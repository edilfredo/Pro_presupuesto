from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ingeniero', 'Ingeniero'),
        ('secretaria', 'Secretaria'),
        ('contadora', 'Contadora'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='secretaria')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# modelo del presupuesto

class Presupuesto(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    unidad = models.CharField(max_length=10)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=2)

    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Presupuesto: {self.nombre}"

class ItemPresupuesto(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE, related_name='items')
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    unidad = models.CharField(max_length=10)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def valor_total(self):
        return self.cantidad * self.valor_unitario

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"