from django.db import models

class UlazniPaket(models.Model):
    paket=models.CharField(max_length=50)
    kvantiteta=models.IntegerField()

