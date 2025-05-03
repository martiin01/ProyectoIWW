from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from producto.models import Producto
from producto.serializers import ProductoSerializer
from .models import Cupon
from .serializers import CuponSerializer


class CuponViewSet(viewsets.ModelViewSet):
    """
    CRUD de Cupones:
      GET    /api/cupones/               → list()
      POST   /api/cupones/               → create()
      GET    /api/cupones/{pk}/          → retrieve()
      PUT    /api/cupones/{pk}/          → update()
      PATCH  /api/cupones/{pk}/          → partial_update()
      DELETE /api/cupones/{pk}/          → destroy()
    """
    queryset         = Cupon.objects.all()
    serializer_class = CuponSerializer

    def perform_create(self, serializer):
        # 1) Guarda el cupón con el usuario que hace la petición
        cupon = serializer.save(usuario=self.request.user)
        # 2) Si llega ?productos=1,2,3 al crear, lo asociamos:
        productos_ids = self.request.query_params.get("productos")
        if productos_ids:
            cupon.productos.set(map(int, productos_ids.split(",")))

    @action(detail=True, methods=["get"], url_path="productos")
    def listar_productos(self, request, pk=None):
        """
        GET /api/cupones/{pk}/productos/
        Devuelve la lista de productos asociados a este cupón.
        """
        cupon = self.get_object()
        productos = cupon.productos.all()

        # opcional: paginar si tienes paginación activa
        page = self.paginate_queryset(productos)
        if page is not None:
            serializer = ProductoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="add_producto")
    def add_producto(self, request, pk=None):
        """
        POST /api/cupones/{pk}/add_producto/  { "producto_id": 12 }
        Añade el producto 12 al cupón pk.
        """
        cupon = self.get_object()
        pid   = request.data.get("producto_id")
        try:
            producto = Producto.objects.get(pk=pid)
        except Producto.DoesNotExist:
            return Response(
                {"detail": "Producto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        cupon.productos.add(producto)
        return Response(
            {"success": f"Producto {pid} añadido al cupón {pk}"},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["post"], url_path="remove_producto")
    def remove_producto(self, request, pk=None):
        """
        POST /api/cupones/{pk}/remove_producto/  { "producto_id": 12 }
        Elimina el producto 12 del cupón pk.
        """
        cupon = self.get_object()
        pid   = request.data.get("producto_id")
        cupon.productos.remove(pid)
        return Response(
            {"success": f"Producto {pid} eliminado del cupón {pk}"},
            status=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        """
        Override para devolver {"success": "ok", "id": nuevo_id}.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cupon = serializer.save(usuario=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"success": "ok", "id": cupon.id},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
