from rest_framework.routers import DefaultRouter
from .views import SedeView

router = DefaultRouter()
router.register(prefix="sede", basename="sede", viewset=SedeView)
