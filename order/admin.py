from django.contrib import admin

# Register your models here.
from .models import orderan

#admin.site.register(daftar)
class orderanAdmin(admin.ModelAdmin):
    list_display = ('pemesan','nama_pesanan', 'jumlah_pesanan','tgl_pesan')
    fields = ['pemesan','nama_pesanan', 'jumlah_pesanan','tgl_pesan']
 
    pass

admin.site.register(orderan, orderanAdmin)