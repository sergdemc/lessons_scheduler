from django.contrib import admin
from .models import SchoolWork


class MonthFilter(admin.SimpleListFilter):
    title = 'Month'
    parameter_name = 'month'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Январь'),
            ('2', 'Февраль'),
            ('3', 'Март'),
            ('4', 'Апрель'),
            ('5', 'Май'),
            ('6', 'Июнь'),
            ('7', 'Июль'),
            ('8', 'Август'),
            ('9', 'Сентябрь'),
            ('10', 'Октябрь'),
            ('11', 'Ноябрь'),
            ('12', 'Декабрь'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(date_sw__month=self.value())


@admin.register(SchoolWork)
class SchoolWorkAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'type_sw', 'date_sw', 'time_sw', 'is_paid', 'is_confirmed', 'event_id', 'created_at')
    list_editable = ('is_paid', 'date_sw', 'time_sw', 'type_sw', 'is_confirmed')
    list_filter = ('type_sw', 'is_paid', MonthFilter)
    search_fields = ('user__telegram_id', 'created_at')
    list_per_page = 10
