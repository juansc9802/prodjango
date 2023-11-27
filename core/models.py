from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# BASE DE DATOS


'''
Informacion de la base de datos: 
1. null = confirma si es el espacio se puede que dar nulo 
2. blank = se confirma si el espacio puede estar en blanco
3. Uniquite = Se asegura que no existan repetidos
    created = models.DateTimeField(auto_now_add=True) confirma fecha creada
    created = models.DateTimeField(auto_now_add=True) confirma fecha actualizada
'''
class Guarderias(models.Model):
    codigo= models.CharField(max_length=200, unique=True, null = False, blank=False)
    nombre= models.CharField(max_length=200, null = True, blank=True)
    telefono= models.CharField(max_length=200, null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    costo = models.DecimalField(max_digits=25, decimal_places=2, null=False)
    imagen = models.ImageField(upload_to='guarderias/', null=True, blank=True)
    descrip = models.TextField (max_length=400, null = True, blank=True)
    direccion = models.CharField(max_length=200, null = True, blank=True)
    correoElec = models.CharField(max_length=200, null = True, blank=True)
    disponibilidad = models.IntegerField(default=20)
    class Meta:
        verbose_name = 'guarderia'
        verbose_name_plural = 'guarderias'

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle_guarderia', args=[str(self.id)])
    
class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('Aprobado', 'Aprobado'),
        ('Cancelado', 'Cancelado'),
        ('Rechazado', 'Rechazado'),
        ('Pendiente', 'Pendiente'),
    ]
    id = models.AutoField(primary_key=True)
    guarderia = models.ForeignKey(Guarderias, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    f_inicio = models.DateField()
    f_fin = models.DateField()
    hora_inicio = models.TimeField(default='00:00')    
    hora_fin = models.TimeField(default='00:00') 
    mascota = models.CharField(max_length=200, null = True, blank=True)
    responsable = models.CharField(max_length=200, null = True, blank=True)
    descrip = models.TextField (max_length=200, null = True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')



    class Meta:
        verbose_name = 'reserva'
        verbose_name_plural = 'reservas'

    
