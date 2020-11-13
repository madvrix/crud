from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.ordering, name='ordering'),
    path('tambah2/', views.add2),
    path('<id>/edit2', views.update2),
    path('<id>/dell2', views.dell2),
]