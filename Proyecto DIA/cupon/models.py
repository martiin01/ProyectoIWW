from django.db import models
from user.models import User

# Create your models here.
class Cupon(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name