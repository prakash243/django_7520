from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [

    path('', views.todo, name="todo"),
    path('addtodo/', views.addtodo, name="addtodo"),
    path('completeTodo/<int:todo_id>', views.completeTodo, name="completeTodo"),
    path('deleteCompleted/', views.deleteCompleted, name="deleteCompleted"),
    path('deleteAll/', views.deleteAll, name="deleteAll"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('edit/', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),


]