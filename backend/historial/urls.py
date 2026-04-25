from rest_framework.routers import DefaultRouter
from .views import HistorialViewSet

router = DefaultRouter()
router.register(r'historial', HistorialViewSet)

urlpatterns = router.urls