from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import EnrollmentViewSet

router = SimpleRouter()
router.register("enrollments", EnrollmentViewSet, basename="enrollments")

urlpatterns = router.urls
