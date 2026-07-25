from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('add/', views.activity_create, name='activity_create'),
    path('edit/<int:pk>/', views.activity_update, name='activity_update'),
    path('delete/<int:pk>/', views.activity_delete, name='activity_delete'),
]
