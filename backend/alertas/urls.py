from rest_framework.routers import DefaultRouter
from .views import AlertaViewSet

router = DefaultRouter()
router.register(r'alertas', AlertaViewSet)

urlpatterns = router.urls