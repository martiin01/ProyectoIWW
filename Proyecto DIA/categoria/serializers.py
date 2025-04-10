from rest_framework import serializers
from .models import Categoria

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ( 'idCategoria', 'name_Categoria', 'description')