from django.shortcuts import render, redirect
from .models import Todo, Comments
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .utils import upload_and_save
# Create your views here.

def index(request):
    todos = Todo.objects.all().order_by('due')
    return render(request, 'index.html', { 'todos' : todos })

def detail(request, key):
    todo = Todo.objects.get(pk = key)

    if request.method == "POST":
        Comments.objects.create(
            todo = todo,
            comment = request.POST['comment'],
            author = request.user
        )
        
        return redirect('detail', key)
    return render(request, 'detail.html', {'todo' : todo})

@login_required(login_url = '/registration/login')
def new(request):
    if request.method == 'POST':
        print(request.POST)
        file_to_upload = request.FILES.get('img')
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due'],
            author = request.user,
            img = upload_and_save(request, file_to_upload)
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

def delete_comment(request, key, comment_key):
    comment = Comments.objects.get(pk = comment_key)
    comment.delete()
    return redirect('detail', key)

def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username = request.POST['username'])
        if len(found_user) > 0:
            error = 'username already exists'
            return render(request, 'registration/signup.html', {'error' : error})
        
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user, backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    return render(request, 'registration/signup.html')
 
def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = 'Incorrect ID or Password'
            return render(request, 'registration/login.html', {'error': error})
            
        auth.login(request, found_user, backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next', '/'))
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def mypage(request, mykey):
    todos = Todo.objects.filter(author = request.user)
    return render(request, 'mypage.html', {'todos' : todos})
    

