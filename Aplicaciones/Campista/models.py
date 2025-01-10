from django.db import models

# Create your models here.
class Campista(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    direccion = models.TextField()

#==========MODELO DE RESERVA=======================
class Reserva(models.Model):
    TIPO_ALOJAMIENTO_CHOICES = [
        ('Tienda', 'Tienda'),
        ('Cabaña', 'Cabaña'),
        ('Caravana', 'Caravana'),
    ]
    ESTADO_RESERVA_CHOICES = [
        ('Confirmada', 'Confirmada'),
        ('Pendiente', 'Pendiente'),
        ('Cancelada', 'Cancelada'),
    ]

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    campista = models.ForeignKey(Campista, on_delete=models.CASCADE)
    tipo_alojamiento = models.CharField(max_length=20, choices=TIPO_ALOJAMIENTO_CHOICES)
    numero_personas = models.PositiveIntegerField()
    estado_reserva = models.CharField(max_length=20, choices=ESTADO_RESERVA_CHOICES)
    observaciones = models.TextField(blank=True, null=True)