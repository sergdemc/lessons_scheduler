from django.urls import path
from .views import UserLoginView, UserLogoutView, UserCreateView

urlpatterns = [

    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/logout/', UserLogoutView.as_view(), name='logout'),
    path('user/create/', UserCreateView.as_view(), name='register'),

]
