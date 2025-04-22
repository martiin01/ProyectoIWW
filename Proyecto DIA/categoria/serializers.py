from rest_framework import serializers
from .models import Categoria

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ( 'pk','idCategoria', 'name_Categoria', 'description')