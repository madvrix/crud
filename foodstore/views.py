from django.shortcuts import render, redirect
from foodstore import models

# Create your views here.
# def index(request):

#     """View function for home page of site."""

#     # Generate counts of some of the main objects
#     num_daftar = daftar.objects.all().count()
    
#     context = {
#         'num_daftar': num_daftar,        
#     }

#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'index.html', context=context)
def index(request):
    task = models.daftar.objects.all()
    return render(request, 'index.html',{ 
        'data' : task,
    })

def add(request):
    if request.POST:
        models.daftar.objects.create(
        nama_makanan=request.POST['nama_makanan'],
        jumlah=request.POST['jumlah'],
        harga=request.POST['harga'],
        produksi=request.POST['produksi'],
        exp=request.POST['exp'],)
        return redirect('index')
    task = models.daftar.objects.all()
    return render(request, 'tambah.html',
    { 'data' : task,
    })

def update(request, id):
    if request.POST:
        models.daftar.objects.filter(pk=id).update(
        nama_makanan=request.POST['nama_makanan'],
        jumlah=request.POST['jumlah'],
        harga=request.POST['harga'],
        produksi=request.POST['produksi'],
        exp=request.POST['exp'],)
        return redirect('index')
    task = models.daftar.objects.filter(pk=id).first()
    return render(request, 'edit.html',
    { 'data' : task,
    })

def dell(request, id):
    task = models.daftar.objects.filter(pk=id).delete()
    return redirect('index')