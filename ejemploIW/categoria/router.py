from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


# Creating a new router object.
routerCategorias = DefaultRouter()
# Registering the viewset to the router.
routerCategorias.register(prefix="categoria", basename="categoria", viewset=CategoriaView)
