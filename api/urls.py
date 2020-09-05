from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', views.CustomerView)
router.register('person', views.person)

urlpatterns = [
  
  path('class/', include(router.urls)),

  # Api for .Customer model using function INDIVIDUALLY
  path('customer_listind/', views.Customer_list_seprately), 
  path('customer_add/', views.add),
  path('customer_update/<int:id>/', views.update),
  path('customer_delete/<int:id>/', views.delete),

# Api for .Customer model using function COMBINED
  path('customer/', views.Customer_list),
  path('customer/<int:id>/', views.update_delete),
  
  # Api for Crud.Person model using function COMBINED
  path('person_list/', views.person_list_function),
  path('person_list/<int:id>/', views.person_update_delete),

  ]