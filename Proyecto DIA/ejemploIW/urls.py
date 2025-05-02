# ejemploIW/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from producto.router import router as routerProductos
from sede.router     import router as routerSedes
from categoria.router     import router as routerCategoria
from user import views as user_views

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework.routers import DefaultRouter

# Routers de cada app
from producto.router import router as routerProductos
from sede.router    import router as routerSedes

# Tu ViewSet de cupones
from cupon.views import CuponViewSet

# Creamos un router nuevo solo para cupones
routerCupon = DefaultRouter()
routerCupon.register(r'cupones', CuponViewSet, basename='cupon')

urlpatterns = [

    path(
      "",
      RedirectView.as_view(url="/docs/", permanent=False),
      name="root-redirect"
    ),
    # Admin de Django
    path('admin/', admin.site.urls),

    # Documentación OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/',      SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/',     SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Endpoints de usuario
    path('api/user/',         user_views.Users_list,   name='user-list'),
    path('api/user/<int:pk>/', user_views.Users_detail, name='user-detail'),

    # APIs de producto, sede y cupon
    path('api/', include(routerProductos.urls)),
    path('api/', include(routerSedes.urls)),
    path('api/', include(routerCupon.urls)),

    path('api/', include(routerProductos.urls)),
    path('api/', include(routerSedes.urls)),
    path('api/', include(routerCupon.urls)),
    path("api/", include(routerCategoria.urls))

]
