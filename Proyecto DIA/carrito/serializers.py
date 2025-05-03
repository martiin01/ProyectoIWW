# carrito/serializers.py
from rest_framework import serializers

from producto.models import Producto
from .models import Carrito, CarritoItem
from producto.serializers import ProductoSerializer

class CarritoItemSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        write_only=True,
        source="producto"
    )

    class Meta:
        model = CarritoItem
        fields = ["id", "producto", "producto_id", "cantidad"]

class CarritoSerializer(serializers.ModelSerializer):
    items = CarritoItemSerializer(many=True)

    class Meta:
        model = Carrito
        fields = ["id", "items", "updated"]
