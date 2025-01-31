"""TODO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basictodo import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('signup/',views.signupuser,name='signupuser'),
    path('login/',views.loginuser,name='loginuser'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('create/',views.createtodo,name='createtodo'),
    path('current/',views.current,name='current'),
    path('completed',views.completedtodo,name='completedtodo'),
    path('todo/<int:todo_pk>/',views.viewtodo,name='viewtodo'),
    path('todo/<int:todo_pk>/complete/',views.todocomplete,name='todocomplete'),
    path('todo/<int:todo_pk>/delete',views.tododelete,name='tododelete'),
]
