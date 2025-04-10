from rest_framework import serializers
from .models import Cupon

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cupon 
        fields = ( 'idCupon', 'name_Cupon', 'description')