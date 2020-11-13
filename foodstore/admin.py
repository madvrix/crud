from django.contrib import admin

# Register your models here.

from .models import daftar

#admin.site.register(daftar)
class daftarAdmin(admin.ModelAdmin):
    list_display = ('nama_makanan','harga', 'jumlah','exp')
    fields = ['nama_makanan','harga', 'jumlah',('produksi', 'exp')]
 
    pass

admin.site.register(daftar, daftarAdmin)
