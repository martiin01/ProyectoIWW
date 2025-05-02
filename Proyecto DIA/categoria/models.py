from django.db import models
from django.conf import settings   # para referenciar al user via AUTH_USER_MODEL

class Categoria(models.Model):
    # ─── Quién la creó ───────────────────────────────────────
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="categorias",
    )

    # ─── Datos de la categoría ───────────────────────────────
    nombre      = models.CharField(
        max_length=100,
        unique=True,
        help_text="Nombre identificador de la categoría"
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        help_text="Texto descriptivo opcional"
    )

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
