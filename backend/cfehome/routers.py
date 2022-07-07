from rest_framework.routers import DefaultRouter

from products.viewsets import ProductGenericViewSet

router = DefaultRouter()
router.register('products', ProductGenericViewSet,
basename='products')
# print(router.urls) # Printing this out shows only two endpoints
urlpatterns = router.urls