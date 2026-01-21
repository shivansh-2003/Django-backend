from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from .permissions import IsInstructorOrAdmin
from apps.organizations.models import OrganizationMember
from apps.enrollments.models import Enrollment


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsInstructorOrAdmin]

    def get_queryset(self):
        membership = OrganizationMember.objects.filter(
            user=self.request.user,
            organization=self.request.organization,
        ).first()

        queryset = Course.objects.filter(
            organization=self.request.organization
        )

        if membership and membership.role == "STUDENT":
            queryset = queryset.filter(
                enrollments__user=self.request.user,
                enrollments__status=Enrollment.Status.ACTIVE,
            )

        return queryset.select_related("organization", "created_by").distinct()

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.organization,
            created_by=self.request.user,
        )


class LessonViewSet(ModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsInstructorOrAdmin]

    def get_queryset(self):
        return Lesson.objects.filter(
            course__id=self.kwargs["course_id"],
            course__organization=self.request.organization,
        ).select_related("course")

    def perform_create(self, serializer):
        course = Course.objects.get(
            id=self.kwargs["course_id"],
            organization=self.request.organization,
        )
        serializer.save(course=course)
