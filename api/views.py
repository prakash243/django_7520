from django.shortcuts import render, redirect
from Crud.models import Person
from .models import Customer
from .serializers import CustomerSerializer, PersonSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response 
from rest_framework.decorators import api_view
# from rest_framework.status import status



# Api for .Customer model using Class Based Views
class CustomerView(ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  
  
# Api for .Customer model using function INDIVIDUALLY (means seperately defined function)
@api_view(['GET'])
def Customer_list_seprately(request):
  obj = Customer.objects.all()
  serializer = CustomerSerializer(obj, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def add(request):
  if request.method == 'POST':
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)     

@api_view(['PUT'])   
def update(request,id):
  ins = Customer.objects.get(id=id)
  serializer = CustomerSerializer(instance=ins,data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.data)
  
@api_view(['DELETE'])
def delete(request,id):
  ins = Customer.objects.get(id=id)
  ins.delete()
  return Response("{} is successfully deleted".format(ins))



# Api for .Customer model using function COMBINED
@api_view(['GET', 'POST'])
def Customer_list(request):
  obj = Customer.objects.all()
  serializer = CustomerSerializer(obj, many=True)
  
  if request.method == 'POST':
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
  return Response(serializer.data)
  
  
@api_view(['GET', 'PUT', 'DELETE'])
def update_delete(request,id):
  ins = Customer.objects.get(id=id)
  serializer = CustomerSerializer(ins, many=False)
  if request.method == "PUT":
    serializer = CustomerSerializer(instance=ins, data=request.data)
    if serializer.is_valid():
      serializer.save()    
  elif request.method== "DELETE":
    ins.delete()

  return Response (serializer.data)

# Api for .Customer model using function COMBINED
#  _______________END_____________________


# Api for Crud.Person model using Class Based Views 
class person(ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
    
# Api for Crud.Person model using function COMBINED
@api_view(['GET', 'POST'])
def person_list_function(request):
  person_obj = Person.objects.all()
  person_serialize = PersonSerializer(person_obj, many=True)
  
  if request.method == 'POST':
    person_serialize = PersonSerializer(data=request.data)
    if person_serialize.is_valid():
      person_serialize.save()      
  return Response (person_serialize.data)

@api_view(["GET", "PUT", "DELETE"])
def person_update_delete(request, id):
  person_instance = Person.objects.get(id=id)
  person_serialize = PersonSerializer(instance=person_instance, many=False)
  print(person_serialize)
  if request.method == "PUT":
    person_serialize = PersonSerializer(instance=person_instance, data=request.data)
    if person_serialize.is_valid():
      person_serialize.save()      
  elif request.method == "DELETE":
    person_instance.delete()
    return Response("{} is successfully deleted".format(person_instance))   
  return Response (person_serialize.data)
      
# Api for Crud.Person model using function
#  _______________END_____________________