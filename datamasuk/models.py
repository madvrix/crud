from django.db import models

# Create your models here.
class datamasuk(models.Model):
    
    makanan=models.CharField(max_length=225)
    jumlah_masuk = models.IntegerField()
    tgl_masuk = models.DateField()
    
    
    class Meta:
        ordering = ['tgl_masuk']

    def __str__(self):
        return self.tgl_masuk