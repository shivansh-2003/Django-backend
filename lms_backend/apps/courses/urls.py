from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CourseViewSet, LessonViewSet

router = SimpleRouter()
router.register("courses", CourseViewSet, basename="courses")

urlpatterns = router.urls + [
    path(
        "courses/<int:course_id>/lessons/",
        LessonViewSet.as_view({"get": "list", "post": "create"}),
    ),
]
