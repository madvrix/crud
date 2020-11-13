from django.db import models

class daftar(models.Model):
    
    nama_makanan = models.CharField(max_length=255)
    jumlah = models.IntegerField()
    harga = models.IntegerField()
    produksi = models.DateField(null=True)
    exp = models.DateField(null=True)
    
    class Meta:
        ordering = ['nama_makanan']

    def __str__(self):
        return self.nama_makanan