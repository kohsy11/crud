from django.shortcuts import render, redirect
from .models import Todo
import datetime
# Create your views here.

def index(request):
    todos = Todo.objects.all().order_by('due')
    return render(request, 'index.html', { 'todos' : todos })

def detail(request, key):
    todo = Todo.objects.get(pk = key)
    return render(request, 'detail.html', { 'todo' : todo })

def new(request):
    if request.method == 'POST':
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due']
        )
        return redirect('detail', new_todo.pk)
    return render(request, 'new.html')

def edit(request, key):
    todo = Todo.objects.get(pk = key)
    if request.method == 'POST':
        Todo.objects.filter(pk=key).update(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due']
        )
        return redirect('detail', key)
    return render(request, 'edit.html', {'todo' : todo } )

def delete(request, key):
    todo = Todo.objects.get(pk = key)
    todo.delete()
    return redirect('index')
