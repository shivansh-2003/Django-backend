from django.urls import path
from .views import CourseAnalyticsView, StudentCourseProgressView

urlpatterns = [
    path(
        "courses/<int:course_id>/analytics/",
        CourseAnalyticsView.as_view(),
    ),
    path(
        "courses/<int:course_id>/progress/",
        StudentCourseProgressView.as_view(),
    ),
]
