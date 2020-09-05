from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def todo(request):
    form = TodoForm()
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list, 'form':form}
    return render(request, 'todo.html', context)

def addtodo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(todo)
    else:
        return render(request, 'update.html', {'form':form})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('todo')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('todo')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('todo')


def edit(request):
    form = TodoForm()
    return render(request,'update.html', {'form':form})

def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        todo.save()
        return redirect('todo')
    return render(request, 'update.html', {'form':form})





