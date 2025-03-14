from celery.schedules import crontab
from flask import current_app as app
from application.celery.tasks import email_reminder_to_professionals, email_report_to_customers


celery_app = app.extensions['celery']

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # sender.add_periodic_task(time_in_sec, function.s(parameter), name="uniquely_identify")

    sender.add_periodic_task(crontab(hour=10, minute=41), email_reminder_to_professionals.s())

    sender.add_periodic_task(crontab(hour=10, minute=41, day_of_month=14), email_report_to_customers.s())
