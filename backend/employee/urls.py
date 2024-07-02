from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('employee_list', employee_list, name='employee_list'),
    path('get_employee/<int:pk>', get_employee, name='get_employee'),
    path('create_employee', create_employee, name='create_employee'),
    path('update_employee/<int:pk>', update_employee, name='update_employee'),
    path('delete_employee/<int:pk>', delete_employee, name='delete_employee'),
    path('add_employee', add_employee, name='add_employee'),
    path('list_employees', list_employees, name='list_employees'),

    path('employee_type_list', employee_type_list, name='employee_type_list'),
    path('get_employee_type/<int:pk>', get_employee_type, name='get_employee_type'),
    path('create_employee_type', create_employee_type, name='create_employee_type'),
    path('update_employee_type/<int:pk>', update_employee_type, name='update_employee_type'),
    path('delete_employee_type/<int:pk>', delete_employee_type, name='delete_employee_type'),

    # Created Exam urls by Kunal Durudkar

    path('add_subject/', views.add_subject),
    path('search_subject', views.search_subject),
    path('update_subject/<int:id>', views.update_subject),
    path('delete_subject/<int:id>', views.delete_subject),

    path('add_question/', views.add_question),
    path('search_question_bank', views.search_question_bank),
    path('update_question_bank/<int:id>', views.update_question_bank),
    path('delete_question_bank/<int:id>', views.delete_question_bank),

    path('create_paper/', views.download_questions, name='download_questions'),
]
