from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('sections_create/', views.section_create, name='section_create'),
    path('search_section/', views.search_section, name='search_section'),
    path('update_section/<int:id>/', views.update_section, name='update_section'),
    path('delete_section/<int:id>/', views.delete_section, name='delete_section'),

    path('class_create/', views.std_class_create, name='std_class_create'),
    path('search_stdclass/', views.search_stdclass, name='search_stdclass'),
    path('update_stdclass/<int:id>/', views.update_stdclass, name='update_stdclass'),
    path('delete_stdclass/<int:id>/', views.delete_stdclass, name='delete_stdclass'),

    path('religions_create/', views.religion_create, name='religion_create'),
    path('search_religion/', views.search_religion, name='search_religion'),
    path('update_religion/<int:id>/', views.update_religion, name='update_religion'),
    path('delete_religion/<int:id>/', views.delete_religion, name='delete_religion'),

    path('casteMain_create/', views.maincaste_create, name='casteMain_create'),
    path('search_maincaste/', views.search_maincaste, name='search_maincaste'),
    path('update_maincaste/<int:id>/', views.update_maincaste, name='update_maincaste'),
    path('delete_maincaste/<int:id>/', views.delete_maincaste, name='delete_maincaste'),

    path('casteSub_create/', views.subcaste_create, name='casteSub_create'),
    path('search_subcaste/', views.search_subcaste, name='search_subcaste'),
    path('update_subcaste/<int:id>/', views.update_subcaste, name='update_subcaste'),
    path('delete_subcaste/<int:id>/', views.delete_subcaste, name='delete_subcaste'),

    path('state_create', views.state_create, name='state_create'),
    path('search_state/', views.search_state, name='search_state'),
    path('update_state/<int:id>/', views.update_state, name='update_state'),
    path('delete_state/<int:id>/', views.delete_state, name='delete_state'),

    path('city_create', views.city_create, name='city_create'),
    path('search_city/', views.search_city, name='search_city'),
    path('update_city/<int:id>/', views.update_city, name='update_city'),
    path('delete_city/<int:id>/', views.delete_city, name='delete_city'),

    path('create_tehsil', views.create_tehsil, name='create_tehsil'),
    path('search_tehsil/', views.search_tehsil, name='search_tehsil'),
    path('update_tehsil/<int:id>/', views.update_tehsil, name='update_tehsil'),
    path('delete_tehsil/<int:id>/', views.delete_tehsil, name='delete_tehsil'),

    path('nationality_create', views.nationality_create, name='nationality_create'),
    path('search_nationality/', views.search_nationality, name='search_nationality'),
    path('update_nationality/<int:id>/', views.update_nationality, name='update_nationality'),
    path('delete_nationality/<int:id>/', views.delete_nationality, name='delete_nationality'),

    path('mothertongue_create', views.mothertongue_create, name='mothertongue_create'),
    path('search_mothertongue/', views.search_mothertongue, name='search_mothertongue'),
    path('update_mothertongue/<int:id>/', views.update_mothertongue, name='update_mothertongue'),
    path('delete_mothertongue/<int:id>/', views.delete_mothertongue, name='delete_mothertongue'),

    path('schoolboard_create', views.schoolboard_create, name='schoolboard_create'),
    path('search_schoolboard/', views.search_schoolboard, name='search_schoolboard'),
    path('update_schoolboard/<int:id>/', views.update_schoolboard, name='update_schoolboard'),
    path('delete_schoolboard/<int:id>/', views.delete_schoolboard, name='delete_schoolboard'),

    path('student_create', views.student_create, name='add_student'),
    path('search_student/', views.search_student, name='search_student'),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),

    path('previous_school_create/', previous_school_create, name='previous_school_create'),
    path('search_previousschool/', views.search_previousschool, name='search_previousschool'),
    path('update_previousschool/<int:id>/', views.update_previousschool, name='update_previousschool'),
    path('delete_previousschool/<int:id>/', views.delete_previousschool, name='delete_previousschool'),


    # APIs urls below

    path('section_create_api', views.section_create_api, name='add_section_api'),
    path('section_search_byid_api/<int:pk>/', views.section_search_byid_api, name='get_section_id_api'),
    path('section_search_api', views.section_search_api, name='get_all_section_api'),
    path('section_update_api/<int:pk>/', views.section_update_api, name='update_section_api'),
    path('section_delete_api/<int:pk>/', views.section_delete_api, name='delete_section_api'),

    path('stdclass_create_api', views.stdclass_create_api, name='add_stdclass_api'),
    path('stdclass_search_byid_api/<int:pk>/', views.stdclass_search_byid_api, name='get_stdclass_id_api'),
    path('stdclass_search_api', views.stdclass_search_api, name='get_all_stdclass_api'),
    path('stdclass_update_api/<int:pk>/', views.stdclass_update_api, name='update_stdclass_api'),
    path('stdclass_delete_api/<int:pk>/', views.stdclass_delete_api, name='delete_stdclass_api'),

    path('religion_create_api', views.religion_create_api, name='add_religion_api'),
    path('religion_search_byid_api/<int:pk>/', views.religion_search_byid_api, name='get_religion_id_api'),
    path('religion_search_api', views.religion_search_api, name='get_all_religion_api'),
    path('religion_update_api/<int:pk>/', views.religion_update_api, name='update_religion_api'),
    path('religion_delete_api/<int:pk>/', views.religion_delete_api, name='delete_religion_api'),

    path('maincaste_create_api', views.maincaste_create_api, name='add_maincaste_api'),
    path('maincaste_search_byid_api/<int:pk>/', views.maincaste_search_byid_api, name='get_maincaste_id_api'),
    path('maincaste_search_api', views.maincaste_search_api, name='get_all_maincaste_api'),
    path('maincaste_update_api/<int:pk>/', views.maincaste_update_api, name='update_maincaste_api'),
    path('maincaste_delete_api/<int:pk>/', views.maincaste_delete_api, name='delete_maincaste_api'),

    path('subcaste_create_api', views.subcaste_create_api, name='add_subcaste_api'),
    path('subcaste_search_byid_api/<int:pk>/', views.subcaste_search_byid_api, name='get_subcaste_id_api'),
    path('subcaste_search_api', views.subcaste_search_api, name='get_all_subcaste_api'),
    path('subcaste_update_api/<int:pk>/', views.subcaste_update_api, name='update_subcaste_api'),
    path('subcaste_delete_api/<int:pk>/', views.subcaste_delete_api, name='delete_subcaste_api'),


    path('state_create_api', views.state_create_api, name='add-state-api'),
    path('state_search_api', views.state_search_api, name='get-state-api'),
    path('state_update_api/<int:pk>/', views.state_update_api, name='update-state-api'),
    path('state_delete_api/<int:pk>/', views.state_delete_api, name='delete-state-api'),

    path('city_create_api', views.city_create_api, name='add-city-api'),
    path('city_search_api', views.city_search_api, name='get-city-api'),
    path('city_update_api/<int:pk>/', views.city_update_api, name='update-city-api'),
    path('city_delete_api/<int:pk>/', views.city_delete_api, name='delete-city-api'),

    path('student_create_api', views.student_create_api, name='add_student_api'),
    path('student_search_byid_api/<int:pk>/', views.student_search_byid_api, name='get_student_id_api'),
    path('student_search_api', views.student_search_api, name='get_all_student_api'),
    path('student_update_api/<int:pk>/', views.student_update_api, name='update_student_api'),
    path('student_delete_api/<int:pk>/', views.student_delete_api, name='delete_student_api'),

    path('api_previous_school_create/', previous_school_create_api, name='previous_school_create_api'),
    path('api_previous_school_search/<int:pk>/', previous_school_search_byid_api,
         name='previous_school_search_byid_api'),
    path('api_previous_school_search/', previous_school_search_api, name='previous_school_search_api'),
    path('api_previous_school_update/<int:pk>/', previous_school_update_api, name='previous_school_update_api'),
    path('api_previous_school_delete/<int:pk>/', previous_school_delete_api, name='previous_school_delete_api'),

]
