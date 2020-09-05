from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.newcrud, name="newcrud"),
    # path('submit/', views.submit, name="submit"),
    path('create/', views.create, name="create"),
    # path('read/', views.read, name="read"),
    # path('update/<int:id>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('delete1/', views.delete1, name="delete1"), 
   
   path('scraping/', views.add_scraper)
]
