from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telegram_id = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Telegram ID'
    )
    is_student = models.BooleanField(
        default=False,
        verbose_name='Student'
    )

    def __str__(self):
        return self.telegram_id
