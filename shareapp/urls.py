"""xpShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from shareapp.views import *

urlpatterns = [
    path('', getIndex, name='index'),
    path('author/<name>', getProfile, name='author'),
    path('article/<int:id>',getSingle, name = 'article'),
    path('topic/<name>',getTopic, name = 'topic'),
    path('login',getLogin, name = 'login'),
    path('logout',getLogout, name = 'logout'),
    path('create',getCreate, name = 'create'),
    path('profile',getSeperateProfile, name = 'profile'),
    path('update/<int:id>',getUpdate, name = 'update'),
    path('delete/<int:id>',getDelete, name = 'delete'),




]
