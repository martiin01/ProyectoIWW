from django.db import models

class Cupon(models.Model):
    code = models.CharField(max_length=20, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    # ── Relación Many‑to‑Many ──
    productos = models.ManyToManyField(
        "producto.Producto",       # ← referencia perezosa: evita import circular
        related_name="cupones",    # luego podrás hacer producto.cupones.all()
        blank=True,
    )

    def __str__(self):
        return self.code

    class Meta:
        ordering = ["code"]        # o quita esta línea si no quieres orden
        verbose_name = "Cupón"
        verbose_name_plural = "Cupones"
