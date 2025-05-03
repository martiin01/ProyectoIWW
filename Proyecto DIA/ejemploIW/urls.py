# ejemploIW/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from producto.router   import router as routerProductos
from sede.router       import router as routerSedes
from categoria.router  import router as routerCategoria
from cupon.views       import CuponViewSet
from carrito.views     import CarritoViewSet
from user import views as user_views

# Routers ad‐hoc
routerCupon    = DefaultRouter()
routerCupon.register(r'cupones', CuponViewSet, basename='cupon')

routerCarrito  = DefaultRouter()
routerCarrito.register(r'carrito', CarritoViewSet, basename='carrito')

urlpatterns = [
    path("", RedirectView.as_view(url="/docs/", permanent=False), name="root-redirect"),

    # Admin
    path("admin/", admin.site.urls),

    # Swagger / ReDoc
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/",      SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/",     SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # Usuarios "a mano"
    path("api/user/",        user_views.Users_list,   name="user-list"),
    path("api/user/<int:pk>/", user_views.Users_detail, name="user-detail"),

    # Routers de cada app
    path("api/", include(routerProductos.urls)),
    path("api/", include(routerSedes.urls)),
    path("api/", include(routerCategoria.urls)),
    path("api/", include(routerCupon.urls)),
    path("api/", include(routerCarrito.urls)),
]
