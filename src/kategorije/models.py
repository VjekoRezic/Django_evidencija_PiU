from django.db import models

class Kategorija(models.Model):
    kategorija=models.CharField(max_length=50)
    