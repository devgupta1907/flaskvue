from celery.schedules import crontab
from flask import current_app as app
from application.celery.tasks import email_reminder_to_professionals, email_report_to_customers


celery_app = app.extensions['celery']

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=19, minute=6), email_reminder_to_professionals.s())

    sender.add_periodic_task(crontab(hour=19, minute=3, day_of_month=9), email_report_to_customers.s())
