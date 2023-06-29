from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'telegram_id', 'is_student', 'date_joined')
    list_editable = ('is_student', 'email', 'telegram_id')
    list_filter = ('is_student',)
    search_fields = ('username', 'telegram_id')
    ordering = ('username',)
