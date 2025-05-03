# carrito/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Carrito, CarritoItem
from .serializers import CarritoSerializer, CarritoItemSerializer

class CarritoViewSet(viewsets.GenericViewSet):
    serializer_class = CarritoSerializer

    def get_object(self):
        # obtenemos o creamos el carrito del usuario autenticado
        carrito, _ = Carrito.objects.get_or_create(user=self.request.user)
        return carrito

    def list(self, request):
        """GET /api/carrito/ → ver carrito"""
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

    @action(detail=False, methods=["post"], url_path="add")
    def add(self, request):
        """
        POST /api/carrito/add/
        { "producto_id": 5, "cantidad": 2 }
        """
        carrito = self.get_object()
        data    = request.data
        serializer = CarritoItemSerializer(
            data={**data, "carrito": carrito.id},
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        item, created = CarritoItem.objects.get_or_create(
            carrito=carrito,
            producto=serializer.validated_data["producto"],
            defaults={"cantidad": serializer.validated_data["cantidad"]}
        )
        if not created:
            item.cantidad += serializer.validated_data["cantidad"]
            item.save()
        return Response({"success": True}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="update")
    def update_item(self, request):
        """
        POST /api/carrito/update/
        { "item_id": 12, "cantidad": 3 }
        """
        try:
            item = CarritoItem.objects.get(pk=request.data["item_id"], carrito=self.get_object())
        except CarritoItem.DoesNotExist:
            return Response({"detail":"No existe"}, status=status.HTTP_404_NOT_FOUND)
        item.cantidad = request.data["cantidad"]
        item.save()
        return Response({"success": True})

    @action(detail=False, methods=["post"], url_path="remove")
    def remove_item(self, request):
        """
        POST /api/carrito/remove/ { "item_id": 12 }
        """
        CarritoItem.objects.filter(
            pk=request.data["item_id"], carrito=self.get_object()
        ).delete()
        return Response({"success": True})

    @action(detail=False, methods=["post"], url_path="clear")
    def clear(self, request):
        """POST /api/carrito/clear/ → vacía el carrito"""
        self.get_object().items.all().delete()
        return Response({"success": True})
