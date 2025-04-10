from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


# Creating a new router object.
routerCupones = DefaultRouter()
# Registering the viewset to the router.
routerCupones.register(prefix="cupon", basename="cupon", viewset=CuponView)
