from celery import shared_task
from jinja2 import Environment, FileSystemLoader
import flask_excel
from application.models import ServiceRequest, Professional, Customer
from .mail_service import send_email



@shared_task(ignore_result = False)
def add(x, y):
    return x + y


@shared_task(ignore_result = False)
def create_csv():
    resource = ServiceRequest.query.filter_by(status="CLOSED").all()
    column_names = [column.name for column in ServiceRequest.__table__.columns]
    csv_out = flask_excel.make_response_from_query_sets(resource, column_names=column_names, file_type='csv')

    with open('./application/celery/downloads/report.csv', 'wb') as file:
        file.write(csv_out.data)
    
    return 'report.csv'


@shared_task(ignore_result = False)
def email_reminder_to_professionals():
    professionals = Professional.query.all()

    for professional in professionals:
        pending_service_requests = ServiceRequest.query.filter(
            ServiceRequest.professional_id == professional.user_id,
            ServiceRequest.status == "REQUESTED"
        ).count()

        email_id = professional.user.email
        if pending_service_requests > 0:
            name = professional.user.name

            content = f'Hello, Mr. {name}. Hope you are doing good.\n You have {pending_service_requests} pending requests. Please review and accept those requests. Or if you are not available, you can reject them. \n Thank you.'

            send_email(email_id, 'Pending Service Requests', content)
        else:
            send_email(email_id, 'No Pending Service Requests', 'Cool, No pending service requests')


@shared_task(ignore_result = False)
def email_report_to_customers():
    env = Environment(loader=FileSystemLoader('./application/email_templates'))
    template = env.get_template('customer_report.html')
    
    customers = Customer.query.all()

    for customer in customers:
        email_id = customer.user.email
        service_requests = customer.service_requests

        template_data = {
            "customer": customer,
            "service_requests": service_requests
        }

        content = template.render(template_data)

        send_email(email_id, 'Monthly Customer Report', content)
