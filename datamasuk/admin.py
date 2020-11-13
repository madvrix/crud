from django.contrib import admin

# Register your models here.
from .models import datamasuk

#admin.site.register(daftar)
class masukAdmin(admin.ModelAdmin):
    list_display = ('makanan','jumlah_masuk', 'tgl_masuk')
    fields = ['makanan','jumlah_masuk', 'tgl_masuk']
 
    pass

admin.site.register(datamasuk, masukAdmin)