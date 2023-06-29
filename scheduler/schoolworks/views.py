from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

import requests

from .forms import SignUpLessonForm
from .models import SchoolWork
from scheduler.settings import MY_CHAT_ID, BOT_TOKEN


class ApplyLessonView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = SchoolWork
    template_name = 'schoolworks/apply_lesson.html'
    form_class = SignUpLessonForm
    success_url = reverse_lazy('user_schedule')
    success_message = 'You have successfully applied for a lesson. We will contact you soon.'
    extra_context = {'title': 'Apply for a lesson',
                     'button_text': 'Apply'
                     }

    @staticmethod
    def check_free_time(date, time) -> bool:
        return not SchoolWork.objects.filter(date_sw=date, time_sw=time).exists()

    @staticmethod
    def check_weekend(date) -> bool:
        return date.weekday() not in (5, 6)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user

        date_sw = form.cleaned_data['date_sw']
        time_sw = form.cleaned_data['time_sw']
        type_sw = form.cleaned_data['type_sw']
        telegram_id = form.cleaned_data['telegram_id']

        if not self.check_weekend(date_sw):
            form.add_error(None, 'You cannot apply for a lesson on weekends.')
            return self.form_invalid(form)

        if not self.check_free_time(date_sw, time_sw):
            form.add_error(None, 'This time is already taken.')
            return self.form_invalid(form)

        response = super().form_valid(form)
        message = f'From user {telegram_id}. New {type_sw}. Date: {date_sw}, Time: {time_sw}.'
        requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={MY_CHAT_ID}&text={message}')
        return response


class EnrollListView(LoginRequiredMixin, ListView):
    model = SchoolWork
    template_name = 'schoolworks/user_schedule.html'
    context_object_name = 'sw_list'
    extra_context = {'title': 'Your schedule'}
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return SchoolWork.objects.filter(user=self.request.user).order_by('-date_sw', '-time_sw', '-created_at')
