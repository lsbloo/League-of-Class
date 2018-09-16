from django.db import models

# Create your models here.

class Usuarios(models.Model):
    login=models.CharField(max_length=15)
    senha=models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    matricula=models.CharField(max_length=12,blank=True)

