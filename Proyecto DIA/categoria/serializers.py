# categoria/serializers.py

from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    # si quieres mostrar el username en lugar de la PK:
    usuario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Categoria
        # los campos que de verdad tienes en tu modelo:
        fields = [
            "id",           # ó "pk"
            "usuario",      # FK a User
            "nombre",       # CharField
            "descripcion",  # TextField
        ]
