"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Authentication
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    # API endpoints
    path("api/", include("apps.courses.urls")),
    path("api/", include("apps.enrollments.urls")),
    path("api/", include("apps.assessments.urls")),
    path("api/", include("apps.analytics.urls")),
]
