from django.urls import path, include
from .view import HealthCheckAPIView
urlpatterns = [
    path('health/', HealthCheckAPIView.as_view()),
    path('', include('accounts.urls')),
    path('', include('organizations.urls')),
    path('', include('projects.urls')),
    path('', include('tasks.urls')),
]
