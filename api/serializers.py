from rest_framework.serializers import ModelSerializer
from Crud.models import Person
from .models import Customer

class CustomerSerializer(ModelSerializer):
  class Meta:
    model = Customer
    fields = '__all__'
    
class PersonSerializer(ModelSerializer):
  class Meta:
    model = Person
    fields = '__all__'

