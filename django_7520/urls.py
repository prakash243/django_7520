from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('basic/', include('basicapp.urls')),
    path('todo/', include('To_do_App.urls')),
    path('accounts/', include('accounts.urls')),
    path('newcrud/', include('new_crud.urls')),
    path('api/', include('api.urls')),
    path('crud/', include('Crud.urls')),


    
    
]
