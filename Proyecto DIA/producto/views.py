# producto/views.py

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Producto
from .serializers import ProductoSerializer
from cupon.models import Cupon
from cupon.serializers import CuponSerializer  # asegúrate de importarlo


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def perform_create(self, serializer):
        # asigna el usuario y la categoría al crear
        serializer.save(
            usuario=self.request.user,
            categoria_id=self.request.query_params.get("categoria", 1),
        )

    @action(detail=True, methods=["get"], url_path="cupones")
    def listar_cupones(self, request, pk=None):
        """
        GET /api/producto/{pk}/cupones/
        Devuelve la lista de cupones asociados a este producto.
        """
        producto = self.get_object()
        cupones = producto.cupones.all()
        serializer = CuponSerializer(cupones, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], url_path="add_cupon")
    def add_cupon(self, request, pk=None):
        """
        POST /api/producto/{pk}/add_cupon/  { "cupon_id": 7 }
        Añade el cupón 7 al producto.
        """
        producto = self.get_object()
        cid = request.data.get("cupon_id")
        try:
            cupon = Cupon.objects.get(pk=cid)
        except Cupon.DoesNotExist:
            return Response({"detail": "Cupón no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        producto.cupones.add(cupon)
        return Response({"success": f"Cupón {cid} añadido"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="remove_cupon")
    def remove_cupon(self, request, pk=None):
        """
        POST /api/producto/{pk}/remove_cupon/  { "cupon_id": 7 }
        Quita el cupón 7 del producto.
        """
        producto = self.get_object()
        cid = request.data.get("cupon_id")
        producto.cupones.remove(cid)
        return Response({"success": f"Cupón {cid} eliminado"}, status=status.HTTP_200_OK)
