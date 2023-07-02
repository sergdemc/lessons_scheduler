from django.db import models
from datetime import datetime, timedelta
from .gcalendar.calendar_client import calendar_obj
from scheduler.settings import GOOGLE_CALENDAR
from .tasks import send_email_reminder
from users.models import CustomUser


class SchoolWork(models.Model):
    TYPE_CHOICES = (
        ('lesson', 'Lesson'),
        ('consultation', 'Consultation'),
    )
    TIME_CHOICES = (
        (datetime.strptime('10:00', '%H:%M').time(), '10:00'),
        (datetime.strptime('11:00', '%H:%M').time(), '11:00'),
        (datetime.strptime('12:00', '%H:%M').time(), '12:00'),
        (datetime.strptime('13:00', '%H:%M').time(), '13:00'),
        (datetime.strptime('14:00', '%H:%M').time(), '14:00'),
        (datetime.strptime('15:00', '%H:%M').time(), '15:00'),
        (datetime.strptime('16:00', '%H:%M').time(), '16:00'),
    )

    type_sw = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name='Type'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='author'
    )
    homework = models.TextField(
        blank=True,
        null=True,
        verbose_name='Homework'
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name='Paid'
    )
    date_sw = models.DateField(
        verbose_name='Date of sw',
    )
    time_sw = models.TimeField(
        verbose_name='Time of sw',
        choices=TIME_CHOICES
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name='Comment'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )
    is_confirmed = models.BooleanField(
        default=False,
        verbose_name='Confirmed'
    )

    event_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Event ID'
    )

    def save(self, *args, **kwargs):
        if self.pk:
            original_schoolwork = SchoolWork.objects.get(pk=self.pk)
            if not original_schoolwork.is_confirmed and self.is_confirmed:
                event_data = {
                    'summary': f'{self.type_sw.capitalize()} for user: {self.user}',
                    'start': {
                        'dateTime': datetime.combine(self.date_sw, self.time_sw).isoformat(),
                        'timeZone': 'UTC',
                    },
                    'end': {
                        'dateTime': (datetime.combine(self.date_sw, self.time_sw) + timedelta(hours=1)).isoformat(),
                        'timeZone': 'UTC',
                    },
                }
                event = calendar_obj.add_event(GOOGLE_CALENDAR, event_data)
                self.event_id = event['id']

                reminder_task = send_email_reminder.apply_async(
                    (self.pk,),
                    eta=datetime.combine(self.date_sw, self.time_sw) - timedelta(hours=24)
                )

                # Store the task ID
                # self.reminder_task_id = reminder_task.id

            elif original_schoolwork.date_sw != self.date_sw or original_schoolwork.time_sw != self.time_sw:
                event_data = {
                    'summary': f'{self.type_sw.capitalize()} for user: {self.user}',
                    'start': {
                        'dateTime': datetime.combine(self.date_sw, self.time_sw).isoformat(),
                        'timeZone': 'UTC',
                    },
                    'end': {
                        'dateTime': (datetime.combine(self.date_sw, self.time_sw) + timedelta(hours=1)).isoformat(),
                        'timeZone': 'UTC',
                    },
                }
                calendar_obj.update_event(GOOGLE_CALENDAR, self.event_id, event_data)

                reminder_task = send_email_reminder.apply_async(
                    (self.pk,),
                    eta=datetime.combine(self.date_sw, self.time_sw) - timedelta(hours=24)
                )

                # self.reminder_task_id = reminder_task.id

        return super(SchoolWork, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.telegram_id}: {self.type_sw} {self.date_sw} {self.time_sw}"
