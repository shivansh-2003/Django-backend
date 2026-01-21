from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AssessmentViewSet, SubmissionViewSet

router = SimpleRouter()
router.register(r"courses/(?P<course_id>[^/.]+)/assessments", AssessmentViewSet, basename="assessments")

urlpatterns = router.urls + [
    path(
        "assessments/<int:assessment_id>/submit/",
        SubmissionViewSet.as_view({"post": "create", "get": "list"}),
    ),
]
