from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('organization_list', organization_list, name='organization_list'),
    path('get_organization/<int:pk>', get_organization, name='get_organization'),
    path('create_organization', create_organization, name='create_organization'),
    path('update_organization/<int:pk>', update_organization, name='update_organization'),
    path('delete_organization/<int:pk>', delete_organization, name='delete_organization'),
    path('add_organization', add_organization, name='add_organization'),
    path('list_organizations', list_organizations, name='list_organizations'),
    
]