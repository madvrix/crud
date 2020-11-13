from django.shortcuts import render, redirect
from datamasuk import models

def masuk(request):
    task = models.datamasuk.objects.all()
    return render(request, 'datamasukan.html',{ 
        'data' : task,
    })

def add3(request):
    if request.POST:
        models.datamasuk.objects.create(
        makanan=request.POST['makanan'],
        jumlah_masuk=request.POST['jumlah_masuk'],
        tgl_masuk=request.POST['tgl_masuk'],)
        return redirect('masuk')
    task = models.datamasuk.objects.all()
    return render(request, 'tambah3.html',
    { 'data' : task,
    })

def update3(request, id):
    if request.POST:
        models.datamasuk.objects.filter(pk=id).update(
        makanan=request.POST['makanan'],
        jumlah_masuk=request.POST['jumlah_masuk'],
        tgl_masuk=request.POST['tgl_masuk'],)
        return redirect('masuk')
    task = models.datamasuk.objects.filter(pk=id).first()
    return render(request, 'edit3.html',
    { 'data' : task,
    })

def dell3(request, id):
    task = models.datamasuk.objects.filter(pk=id).delete()
    return redirect('masuk')