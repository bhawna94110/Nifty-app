from .views import DailyPriceRecordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'daily-price-record', DailyPriceRecordViewSet, basename='price-record')
urlpatterns = router.urls   