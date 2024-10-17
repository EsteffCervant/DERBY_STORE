from django.db import models

class Patines(models.Model):
    Deporte = models.CharField(max_length=22)
    Marca = models.CharField(max_length=18)
    Talla = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} {self.Deporte} {self.Marca}'