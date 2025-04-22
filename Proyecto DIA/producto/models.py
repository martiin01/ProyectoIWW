from django.db import models
from user.models import User
from cupon.models import Cupon
from categoria.models import Categoria

# Create your models here.
class Producto(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    idCupon = models.ForeignKey(Cupon, on_delete=models.CASCADE, default=1)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    name = models.CharField(blank=False, null=False, max_length=240)
    description = models.CharField(blank=True, null=True, max_length=240)
    price = models.FloatField(blank=False, null=False, default=1)



    def __str__(self):
        return self.name