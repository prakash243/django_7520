from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [

    path('', views.index1, name="index1"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    
]