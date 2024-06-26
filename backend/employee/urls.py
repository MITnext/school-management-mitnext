from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('/employee_list', employee_list, name='employee_list'),
    path('/get_employee/<int:pk>', get_employee, name='get_employee'),
    path('/create_employee', create_employee, name='create_employee'),
    path('/update_employee/<int:pk>', update_employee, name='update_employee'),
    path('/delete_employee/<int:pk>', delete_employee, name='delete_employee'),
    path('/add_employee', add_employee, name='add_employee'),
    path('/list_employees', list_employees, name='list_employees'),
    
    path('/employee_type_list', employee_type_list, name='employee_type_list'),
    path('/get_employee_type/<int:pk>', get_employee_type, name='get_employee_type'),
    path('/create_employee_type', create_employee_type, name='create_employee_type'),
    path('/update_employee_type/<int:pk>', update_employee_type, name='update_employee_type'),
    path('/delete_employee_type/<int:pk>', delete_employee_type, name='delete_employee_type'),
             
]