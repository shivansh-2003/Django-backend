from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MeAPIView

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='jwt_login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('users/me/', MeAPIView.as_view(), name='me'),
]
