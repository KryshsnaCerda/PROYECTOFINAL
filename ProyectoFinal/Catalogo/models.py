from django.db import models

# Create your models here.

class cliente(models.Model):
    correo = models.CharField(primary_key=True, max_length=40)
    nombre = models.CharField(max_length=40) 
    aparterno = models.CharField(max_length=40)
    amaterno = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=40)


    def __str__(self):
        return str(self.nombre)+" "+str(self.aparterno)
    