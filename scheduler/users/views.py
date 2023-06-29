from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from .forms import UserCreateForm


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    success_message = 'You have successfully logged in.'
    form_class = AuthenticationForm
    extra_context = {'title': 'Login', 'button_text': 'Login'}

    def get_success_url(self):
        if self.request.user.is_student:
            return reverse_lazy('user_schedule')
        return reverse_lazy('apply')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    extra_context = {'title': 'Logout', 'button_text': 'Logout'}

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You have successfully logged out.')
        return super().dispatch(request, *args, **kwargs)


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'form.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    success_message = 'You have successfully registered.'
    extra_context = {'title': 'Sign In', 'button_text': 'Sign In'}
