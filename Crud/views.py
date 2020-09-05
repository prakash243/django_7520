from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def crudhome(request):
  persons = Person.objects.order_by('-id')
  print(persons)
  id = request.GET.get('id')
  print(id)
  if id:
    p = Person.objects.get(id=id)
  return render(request, 'crud.html', {'persons':persons, 'p':p if id else None})
  
def addPerson(request):
  a = Person ()
  a.name = request.POST['name']
  a.save()
  return redirect (crudhome)
  
  
def edit(request,id):
  form = PersonForm()
  b = Person.objects.get(id=id)

  form = PersonForm(request.POST or None, instance=b)
  if form.is_valid():
    form.save()
    return redirect (crudhome)
      
  return render(request, 'edit.html', {'form': form})
  
  
def delete(request,id):
  
  b = Person.objects.get(id=id)
  b.delete()
  return redirect (crudhome)
  
  
  
  
  
def update(request):
  id = request.POST.get('id')
  if id:
    c = Person.objects.get(id=id)
  else:
    c = Person()
  c.name = request.POST['name']
  c.save()
  return redirect(crudhome)
      

 
  