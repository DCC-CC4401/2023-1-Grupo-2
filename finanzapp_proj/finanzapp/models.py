from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Usuarios
class User(AbstractUser):
    # Nombre que aparecerá en la página
    display_name = models.CharField(max_length=100, blank=True)
    # Monto, parte en 0
    total = models.FloatField(default=0)
    # Presupuesto, opcional
    budget = models.FloatField(blank=True, null=True)

# Transacciones
class Transaction(models.Model):
    # Tiene un único usuario asociado
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    # Tipos de transacciones
    types = [('spend', 'gasto'), ('deposit', 'abono')]
    type = models.CharField(choices=types, max_length=100)
    # Descripción de la transaccion
    description = models.TextField(max_length=500)
    # Monto de la transacción
    amount = models.FloatField(default=0)
    # Fecha de la transacción
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

# Categorias 
class Category(models.Model):
    # Nombre de la categoria
    name = models.CharField(max_length=100)
    # Presupuesto asociado a la categoria, opcional
    budget = models.FloatField(blank=True)
    # Usuario que creo la categoría
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
