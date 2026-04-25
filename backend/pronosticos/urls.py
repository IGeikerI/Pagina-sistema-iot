from rest_framework.routers import DefaultRouter
from .views import PronosticoViewSet

router = DefaultRouter()
router.register(r'pronosticos', PronosticoViewSet)

urlpatterns = router.urls