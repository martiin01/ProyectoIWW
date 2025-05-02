from django.db import models
from django.conf import settings

class Producto(models.Model):
    usuario   = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="productos",
    )
    categoria = models.ForeignKey(
        "categoria.Categoria",
        on_delete=models.PROTECT,
        related_name="productos",
    )

    nombre        = models.CharField(max_length=240)
    descripcion   = models.TextField(blank=True, null=True)
    precio        = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
