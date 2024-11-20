from django.db import models

class ruedas(models.Model):
    Dureza = models.CharField(max_length=4)
    Perfil = models.CharField(max_length=9)
    Compuesto = models.CharField(max_length=15)
    Talla = models.IntegerField()
    Anio = models.IntegerField(default=2024)
    Fecha_carga = models.DateField(default="2024-01-01")
    
    def __str__(self):
        return f'{self.id} {self.Dureza} {self.Perfil} {self.Anio}'

