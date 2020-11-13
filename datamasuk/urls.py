from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.masuk, name='masuk'),
    path('tambah3/', views.add3),
    path('<id>/edit3', views.update3),
    path('<id>/dell3', views.dell3),
]