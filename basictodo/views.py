from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from basictodo.forms import TodoForm
from basictodo.models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'basictodo/home.html')


def signupuser(request):
    form = UserCreationForm()
    if request.method == 'GET':
        return render(request,'basictodo/signup.html',{'form':form})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('current')
            except IntegrityError:
                return render(request,'basictodo/signup.html',{'form':form,'error':'That username '+ request.POST['username'] + ' has already been taken' })
        else:
            return render(request,'basictodo/signup.html',{'form':form,'error':'Password Didnt Match'})


def loginuser(request):
    form = AuthenticationForm()
    if request.method == 'GET':
        return render(request,'basictodo/loginuser.html',{'form': form})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'basictodo/loginuser.html',{'error':'Username or Password Didnt Match'})
        else:
            login(request,user)
            return redirect('current')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def createtodo(request):
    form = TodoForm()
    if request.method == 'GET':
        return render(request,'basictodo/createtodo.html',{'form':form})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            #print(newtodo['user'])
            newtodo.user = request.user
            print(newtodo.user)
            newtodo.save()
            return redirect('current')
        except ValueError:
            return render(request,'basictodo/createtodo.html',{'error':'Title is having char more than 100'})


@login_required
def current(request):
    todos = Todo.objects.filter(user=request.user,datacompleted__isnull=True)
    return render(request,'basictodo/current.html',{'todos':todos})

@login_required
def completedtodo(request):
    todo = Todo.objects.filter(user=request.user,datacompleted__isnull=False).order_by('-datacompleted')
    print(todo)
    return render(request,'basictodo/completedtodo.html',{'todo':todo})


@login_required
def viewtodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk,user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request,'basictodo/viewtodo.html',{'todo':todo,'form':form})
    else:
        try:
            form = TodoForm(request.POST,instance=todo)
            form.save()
            return redirect('current')
        except ValueError:
            return render(request,'basictodo/viewtodo.html',{'todo':todo,'form':form,'error':'Title is having char more than 100'})


@login_required
def todocomplete(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk,user=request.user)
    if request.method == 'POST':
        todo.datacompleted = timezone.now()
        todo.save()
        return redirect('current')


@login_required
def tododelete(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk,user=request.user)
    todo.delete()
    return redirect('current')
