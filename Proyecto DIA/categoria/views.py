from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Categoria
from .serializers import CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para categorías:
    - GET    /categorias/         → list()
    - POST   /categorias/         → create()
    - GET    /categorias/{pk}/    → retrieve()
    - PUT    /categorias/{pk}/    → update()
    - PATCH  /categorias/{pk}/    → partial_update()
    - DELETE /categorias/{pk}/    → destroy()
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def perform_create(self, serializer):
        # aquí le pasamos el usuario logueado
        serializer.save(usuario=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        Si viene ?select=1,2,3 filtra solo esas categorías por PK;
        si no, devuelve todas.
        """
        qs = self.get_queryset()
        select = request.query_params.get("select")
        if select:
            try:
                pks = [int(x) for x in select.split(",") if x.strip().isdigit()]
                qs = qs.filter(pk__in=pks)
            except ValueError:
                pass  # ignoramos valores no numéricos

        # aplica paginación si está configurada
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Valida y crea una nueva categoría. Devuelve {"success":"ok", "id": <pk>}.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        categoria = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"success": "ok", "id": categoria.id},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
