from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/result/<int:submission_id>/', views.show_result, name='show_result'),
]
