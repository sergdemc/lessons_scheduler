from django.urls import path


from .views import ApplyLessonView, EnrollListView

urlpatterns = [

    path('', ApplyLessonView.as_view(), name='apply'),
    path('enroll/', EnrollListView.as_view(), name='user_schedule'),

]
