from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "telegram_id", "password1", "password2")
