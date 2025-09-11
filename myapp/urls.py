from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>/', views.hello, name='hello'),
    path('project/', views.projects, name='projects'),
    path('tasks/<int:id>/', views.task, name='task'),
]