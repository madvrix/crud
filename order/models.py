from django.db import models

# Create your models here.

class orderan(models.Model):
    
    pemesan=models.CharField(max_length=225)
    nama_pesanan = models.CharField(max_length=255)
    jumlah_pesanan = models.IntegerField()
    tgl_pesan = models.DateField(null=True)
    
    
    class Meta:
        ordering = ['pemesan']

    def __str__(self):
        return self.pemesan