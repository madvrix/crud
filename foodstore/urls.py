from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tambah/', views.add),
    path('<id>/edit', views.update),
    path('<id>/dell', views.dell),
]