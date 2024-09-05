from rest_framework.routers import DefaultRouter

from api_v1.views.products import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, 'products')

urlpatterns = router.urls
