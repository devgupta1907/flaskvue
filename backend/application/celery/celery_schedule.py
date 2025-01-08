from celery.schedules import crontab
from flask import current_app as app
from application.celery.tasks import email_reminder_to_professionals


celery_app = app.extensions['celery']

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=22, minute=57), email_reminder_to_professionals.s())