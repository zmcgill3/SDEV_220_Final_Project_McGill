from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getInput),
    path("enter-employee", views.getInput),
    path("hi", views.Greeting),
    path("add", views.createEmployee),
    path("display", views.createSchedule)
    ]
