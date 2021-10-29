from django.db import models

class Smjena(models.Model):
    iznos=models.DecimalField(decimal_places=2,max_digits=4)
    radnoMjesto=models.CharField(max_length=50)
