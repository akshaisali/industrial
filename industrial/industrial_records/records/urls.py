from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # SQF Material Lists
    path('sqf_80/', views.sqf_80, name='sqf_80'),
    path('sqf_100/', views.sqf_100, name='sqf_100'),
    path('sqf_120/', views.sqf_120, name='sqf_120'),

    # Category Specific Views
    path('tempering/<str:sqf_type>/', views.tempering, name='tempering'),
    path('washing/<str:sqf_type>/', views.washing, name='washing'),
    path('travelser/<str:sqf_type>/', views.travelser, name='travelser'),
    path('crossconveyor/<str:sqf_type>/', views.crossconveyor, name='crossconveyor'),

    # Material Management
    path('material/add/<int:sqf_type>/', views.material_add, name='material_add'),
    path('material/<int:sqf_type>/', views.material_list, name='material_list'),
    path('material/edit/<int:pk>/', views.material_edit, name='material_edit'),
    path('materials/delete/<int:pk>/', views.material_delete, name='material_delete'),

]

