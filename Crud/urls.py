from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.crudhome , name='crudhome'),
    path('addPerson/', views.addPerson, name='addPerson'),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete),
    path('update/', views.update, name='update'),
]
