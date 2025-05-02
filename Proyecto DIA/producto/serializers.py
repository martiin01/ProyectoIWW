# producto/serializers.py

from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    # si quieres mostrar el username en lugar de la PK:
    usuario  = serializers.StringRelatedField(read_only=True)
    categoria = serializers.StringRelatedField(read_only=True)
    # si tienes la relación inversa cupón→producto y la quieres exponer:
    cupones  = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = [
            "id",
            "usuario",
            "categoria",
            "nombre",
            "descripcion",
            "precio",
            "cupones",      # opcional
        ]
