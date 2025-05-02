from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Cupon
from .serializers import CuponSerializer


class CuponViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD de Cupones.
    - GET    /cupon/                → list()
    - POST   /cupon/                → create()
    - GET    /cupon/{pk}/           → retrieve()
    - PUT    /cupon/{pk}/           → update()
    - PATCH  /cupon/{pk}/           → partial_update()
    - DELETE /cupon/{pk}/           → destroy()
    """
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

    def list(self, request, *args, **kwargs):
        """
        Si viene ?select=SALE10,SALE20 filtra solo esos códigos.
        Si no, devuelve todos los cupones.
        """
        select = request.query_params.get("select")
        qs = self.get_queryset()
        if select:
            codes = [c.strip() for c in select.split(",") if c.strip()]
            qs = qs.filter(code__in=codes)

        # Paginación estándar
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Valida y crea un nuevo cupón.
        En caso de éxito devuelve {"success": "ok", "id": <nuevo_id>}.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cupon = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"success": "ok", "id": cupon.id},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
