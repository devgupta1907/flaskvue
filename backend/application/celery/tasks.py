from celery import shared_task
import flask_excel
from application.models import ServiceRequest, Professional
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