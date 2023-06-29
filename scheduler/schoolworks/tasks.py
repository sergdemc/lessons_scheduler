from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(timezone='Europe/Moscow')
def send_email_reminder(schoolwork_id):
    from .models import SchoolWork
    schoolwork = SchoolWork.objects.get(id=schoolwork_id)

    send_mail(
        'Lesson Reminder',
        f'Reminder for your lesson on {schoolwork.date_sw} at {schoolwork.time_sw}',
        settings.DEFAULT_FROM_EMAIL,
        [schoolwork.user.email],
        fail_silently=False,
    )
