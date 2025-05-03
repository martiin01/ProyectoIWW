# categoria/serializers.py
from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    usuario = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Categoria
        fields = ["id", "usuario", "nombre", "descripcion"]
