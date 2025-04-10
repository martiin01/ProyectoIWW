from rest_framework import status
from rest_framework.response import Response
from .models import Cupon
from .serializers import CuponSerializer
from rest_framework import viewsets

# Create your views here.
class CuponView(
    viewsets.ModelViewSet,
):

    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer


    def list(self, request):
        """
        If the action is list, then try to get the query parameter "select" and return the filtered
        queryset. If the query parameter "select" doesn't exist, then return all objects. If the action
        is not list, then return all objects

        :return: List of all products.
        """

        result = Cupon.objects.all()
        return Response(self.serializer_class(result, many=True).data, status=200)

    def create(self, request, *args, **kwargs):
        """
        It creates a new object, then returns a response with a success message

        :param request: The request object

        :return: The response is a dictionary with a key of "success" and a value of "ok."
        """
        try:
            super().create(request, *args, **kwargs)
            return Response({"success": "ok"}, status=201)
        except ValueError:
            return Response({"error": "Invalid date"}, status=400)
