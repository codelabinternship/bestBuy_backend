from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from BestBuy_bot.views import (
    RegisterView, LoginView, index_page, DashboardView,
    CategoryViewSet, ProductViewSet, UserViewSet,
    BotConfigurationViewSet, ReviewViewSet, OrderItemViewSet,
    RoleChoicesViewSet, UserActivityLogsViewSet, SMSCampaignViewSet,
    BranchesViewSet, PaymentMethodsViewSet, VariationsViewSet
)

schema_view = get_schema_view(
   openapi.Info(
      title="BestBuy Backend API",
      default_version='v1',
      description="Dokumentatsiya API uchun BestBuy",
      contact=openapi.Contact(email="example@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
    path('api/auth/login/', LoginView.as_view(), name='auth_login'),

    # Dashboard va API
    path('api/dashboard/', DashboardView.as_view(), name='dashboard'),

    # 💡 SHU YERGA ULANISH QO‘SHILDI
    path('', include('BestBuy_bot.urls')),  # <== MUHIM

    # Swagger va Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Home page (agar bor bo‘lsa)
    path('', index_page),
]
