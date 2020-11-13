from django.shortcuts import render, redirect
from order import models

def ordering(request):
    task = models.orderan.objects.all()
    return render(request, 'order2.html',{ 
        'data' : task,
    })

def add2(request):
    if request.POST:
        models.orderan.objects.create(
        pemesan=request.POST['pemesan'],
        nama_pesanan=request.POST['nama_pesanan'],
        jumlah_pesanan=request.POST['jumlah_pesanan'],
        tgl_pesan=request.POST['tgl_pesan'],)
        return redirect('ordering')
    task = models.orderan.objects.all()
    return render(request, 'tambah2.html',
    { 'data' : task,
    })

def update2(request, id):
    if request.POST:
        models.orderan.objects.filter(pk=id).update(
        pemesan=request.POST['pemesan'],
        nama_pesanan=request.POST['nama_pesanan'],
        jumlah_pesanan=request.POST['jumlah_pesanan'],
        tgl_pesan=request.POST['tgl_pesan'],)
        return redirect('ordering')
    task = models.orderan.objects.filter(pk=id).first()
    return render(request, 'edit2.html',
    { 'data' : task,
    })

def dell2(request, id):
    task = models.orderan.objects.filter(pk=id).delete()
    return redirect('ordering')