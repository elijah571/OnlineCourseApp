from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Course detail page
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    # Enroll in a course
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Submit exam for a course
    path('course/<int:course_id>/submit/', views.submit, name='submit'),

    # Show exam result for a submission
    path('course/<int:course_id>/result/<int:submission_id>/', views.show_result, name='show_result'),
]
