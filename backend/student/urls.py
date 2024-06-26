from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('/sections_create/', views.section_create, name='section_create'),
    path('/section_list/', views.section_list, name='section_list'),
    path('/sections/<int:pk>/', views.section_detail, name='section_detail'),
    path('/sections_update/<int:pk>/', views.section_update, name='section_update'),
    path('/sections_delete/<int:pk>/', views.section_delete, name='section_delete'),

    path('/section_create_api', views.section_create_api, name='add_section_api'),
    path('/section_search_byid_api/<int:pk>/', views.section_search_byid_api, name='get_section_id_api'),
    path('/section_search_api', views.section_search_api, name='get_all_section_api'),
    path('/section_update_api/<int:pk>/', views.section_update_api, name='update_section_api'),
    path('/section_delete_api/<int:pk>/', views.section_delete_api, name='delete_section_api'),

    path('/class_create/', views.std_class_create, name='std_class_create'),
    path('/std_class_list/', views.std_class_list, name='std_class_list'),
    path('/class/<int:pk>/', views.std_class_detail, name='std_class_detail'),
    path('/class_update/<int:pk>/', views.std_class_update, name='std_class_update'),
    path('/class_delete/<int:pk>/', views.std_class_delete, name='std_class_delete'),

    path('/stdclass_create_api', views.stdclass_create_api, name='add_stdclass_api'),
    path('/stdclass_search_byid_api/<int:pk>/', views.stdclass_search_byid_api, name='get_stdclass_id_api'),
    path('/stdclass_search_api', views.stdclass_search_api, name='get_all_stdclass_api'),
    path('/stdclass_update_api/<int:pk>/', views.stdclass_update_api, name='update_stdclass_api'),
    path('/stdclass_delete_api/<int:pk>/', views.stdclass_delete_api, name='delete_stdclass_api'),

    path('/religions_create/', views.religion_create, name='religion_create'),
    path('/religion_list/', views.religion_list, name='religion_list'),
    path('/religions/<int:pk>/', views.religion_detail, name='religion_detail'),
    path('/religions_update/<int:pk>/', views.religion_update, name='religion_update'),
    path('/religions_delete/<int:pk>/', views.religion_delete, name='religion_delete'),

    path('/religion_create_api', views.religion_create_api, name='add_religion_api'),
    path('/religion_search_byid_api/<int:pk>/', views.religion_search_byid_api, name='get_religion_id_api'),
    path('/religion_search_api', views.religion_search_api, name='get_all_religion_api'),
    path('/religion_update_api/<int:pk>/', views.religion_update_api, name='update_religion_api'),
    path('/religion_delete_api/<int:pk>/', views.religion_delete_api, name='delete_religion_api'),

    path('/casteMain_create/', views.maincaste_create, name='casteMain_create'),
    path('/casteMain/', views.maincaste_list, name='casteMain_list'),
    path('/casteMain/<int:pk>/', views.maincaste_detail, name='casteMain_detail'),
    path('/casteMain_update/<int:pk>/', views.maincaste_update, name='casteMain_update'),
    path('/casteMain_delete/<int:pk>/', views.maincaste_delete, name='casteMain_delete'),

    path('/maincaste_create_api', views.maincaste_create_api, name='add_maincaste_api'),
    path('/maincaste_search_byid_api/<int:pk>/', views.maincaste_search_byid_api, name='get_maincaste_id_api'),
    path('/maincaste_search_api', views.maincaste_search_api, name='get_all_maincaste_api'),
    path('/maincaste_update_api/<int:pk>/', views.maincaste_update_api, name='update_maincaste_api'),
    path('/maincaste_delete_api/<int:pk>/', views.maincaste_delete_api, name='delete_maincaste_api'),

    path('/casteSub_create/', views.subcaste_create, name='casteSub_create'),
    path('/casteSub/', views.subcaste_list, name='casteSub_list'),
    path('/casteSub/<int:pk>/', views.subcaste_detail, name='casteSub_detail'),
    path('/casteSub_update/<int:pk>/', views.subcaste_update, name='casteSub_update'),
    path('/casteSub_delete/<int:pk>/', views.subcaste_delete, name='casteSub_delete'),

    path('/subcaste_create_api', views.subcaste_create_api, name='add_subcaste_api'),
    path('/subcaste_search_byid_api/<int:pk>/', views.subcaste_search_byid_api, name='get_subcaste_id_api'),
    path('/subcaste_search_api', views.subcaste_search_api, name='get_all_subcaste_api'),
    path('/subcaste_update_api/<int:pk>/', views.subcaste_update_api, name='update_subcaste_api'),
    path('/subcaste_delete_api/<int:pk>/', views.subcaste_delete_api, name='delete_subcaste_api'),

    path('/state_create', views.state_create, name='state_create'),
    path('/search_state', views.search_state, name='search_state'),
    path('/update_state/<int:id>', views.update_state, name='update_state'),
    path('/delete_state/<int:id>', views.delete_state, name='delete_state'),

    path('/state_create_api', views.state_create_api, name='add-state-api'),
    path('/state_search_api', views.state_search_api, name='get-state-api'),
    path('/state_update_api/<int:pk>/', views.state_update_api, name='update-state-api'),
    path('/state_delete_api/<int:pk>/', views.state_delete_api, name='delete-state-api'),

    path('/city_create', views.city_create, name='city_create'),
    path('/search_city', views.search_city, name='search_city'),
    path('/update_city/<int:pk>', views.update_city, name='update_city'),
    path('/delete_city/<int:pk>', views.delete_city, name='delete_city'),

    path('/city_create_api', views.city_create_api, name='add-city-api'),
    path('/city_search_api', views.city_search_api, name='get-city-api'),
    path('/city_update_api/<int:pk>/', views.city_update_api, name='update-city-api'),
    path('/city_delete_api/<int:pk>/', views.city_delete_api, name='delete-city-api'),

    path('/student_create', views.student_create, name='add_student'),
    path('/student_search', views.student_search, name='get_student'),
    path('/student_update/<int:std_id>', views.student_update, name='update_student'),
    path('/student_delete/<int:std_id>', views.student_delete, name='delete_student'),

    path('/previous_school_create/', previous_school_create, name='previous_school_create'),
    path('/previous_school_search/', previous_school_search, name='previous_school_search'),
    path('/previous_school_update/<int:pk>/', previous_school_update, name='previous_school_update'),
    path('/previous_school-delete/<int:pk>/', previous_school_delete, name='previous_school_delete'),

    path('/student_create_api', views.student_create_api, name='add_student_api'),
    path('/student_search_byid_api/<int:pk>/', views.student_search_byid_api, name='get_student_id_api'),
    path('/student_search_api', views.student_search_api, name='get_all_student_api'),
    path('/student_update_api/<int:pk>/', views.student_update_api, name='update_student_api'),
    path('/student_delete_api/<int:pk>/', views.student_delete_api, name='delete_student_api'),

    path('/api_previous_school_create/', previous_school_create_api, name='previous_school_create_api'),
    path('/api_previous_school_search/<int:pk>/', previous_school_search_byid_api,
         name='previous_school_search_byid_api'),
    path('/api_previous_school_search/', previous_school_search_api, name='previous_school_search_api'),
    path('/api_previous_school_update/<int:pk>/', previous_school_update_api, name='previous_school_update_api'),
    path('/api_previous_school_delete/<int:pk>/', previous_school_delete_api, name='previous_school_delete_api'),

]
