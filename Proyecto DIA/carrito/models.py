# carrito/models.py
from django.conf import settings
from django.db import models
from producto.models import Producto

class Carrito(models.Model):
    user      = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated   = models.DateTimeField(auto_now=True)

class CarritoItem(models.Model):
    carrito   = models.ForeignKey(Carrito, related_name="items", on_delete=models.CASCADE)
    producto  = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad  = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("carrito", "producto")
