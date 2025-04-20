from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, UserViewSet, BotConfigurationViewSet, ReviewViewSet, OrderItemViewSet, RoleChoicesViewSet, UserActivityLogsViewSet, SMSCampaignViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)
router.register(r'bot-configs', BotConfigurationViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'orderitem', OrderItemViewSet)
router.register(r'user-activity-logs', UserActivityLogsViewSet)
router.register(r'sms-campaigns', SMSCampaignViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('rolechoices/', RoleChoicesViewSet.as_view(), name='role-choices')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
