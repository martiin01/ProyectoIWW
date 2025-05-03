from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

# Crea y configura el router
router = DefaultRouter()
router.register(prefix="producto", basename="producto", viewset=ProductoViewSet)

# ¡NO definas ninguna función router() aquí!
