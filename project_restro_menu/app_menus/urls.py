from django.urls import path
from app_menus import views

urlpatterns = [
    path('', views.list_menu, name='menu-list'),
    path('add/', views.add_menu, name='menu-add')
]