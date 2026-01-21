from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import (
    get_course_progress,
    get_course_completion_rate,
)
from apps.courses.models import Course


class CourseAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        course = Course.objects.get(
            id=course_id,
            organization=request.organization,
        )

        data = {
            "course_id": course.id,
            "completion_rate": get_course_completion_rate(course),
        }

        return Response(data)


class StudentCourseProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        course = Course.objects.get(
            id=course_id,
            organization=request.organization,
        )

        progress = get_course_progress(
            student=request.user,
            course=course,
        )

        return Response({
            "course_id": course.id,
            "progress_percent": progress,
        })
