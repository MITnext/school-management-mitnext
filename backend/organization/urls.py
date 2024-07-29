from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register_student/', register_student, name='register_student'),
    path('validate_otp/', validate_otp, name='validate_otp'),
    path('validate-otp-login/', validate_otp_login, name='validate_otp_login'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('principal-dashboard/', principal_dashboard, name='principal_dashboard'),

    path('organization_list', organization_list, name='organization_list'),
    path('get_organization/<int:pk>', get_organization, name='get_organization'),
    path('create_organization', create_organization, name='create_organization'),
    path('update_organization/<int:pk>', update_organization, name='update_organization'),
    path('delete_organization/<int:pk>', delete_organization, name='delete_organization'),
    path('add_organization', add_organization, name='add_organization'),
    path('list_organizations', list_organizations, name='list_organizations'),
    
]