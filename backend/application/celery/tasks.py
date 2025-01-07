from celery import shared_task
import flask_excel
from application.models import ServiceRequest


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
