from rest_framework.routers import DefaultRouter
from .views import ProductoView

# Crea y configura el router
router = DefaultRouter()
router.register(prefix="producto", basename="producto", viewset=ProductoView)

# ¡NO definas ninguna función router() aquí!
