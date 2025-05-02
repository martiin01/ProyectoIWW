# cupon/serializers.py

from rest_framework import serializers
from .models import Cupon
from producto.serializers import ProductoSerializer

class CuponSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Cupon
        fields = [
            "id",
            "code",
            "description",
            "productos",
        ]
