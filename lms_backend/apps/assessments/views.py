from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, PermissionDenied

from .models import Assessment, Submission
from .serializers import AssessmentSerializer, SubmissionSerializer
from .permissions import IsInstructorOrAdmin
from apps.enrollments.models import Enrollment


class AssessmentViewSet(ModelViewSet):
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated, IsInstructorOrAdmin]

    def get_queryset(self):
        return Assessment.objects.filter(
            course__organization=self.request.organization
        ).select_related("course")

    def perform_create(self, serializer):
        serializer.save(course_id=self.kwargs["course_id"])


class SubmissionViewSet(ModelViewSet):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(
            student=self.request.user,
            assessment__course__organization=self.request.organization,
        )

    def perform_create(self, serializer):
        assessment = Assessment.objects.get(
            id=self.kwargs["assessment_id"],
            course__organization=self.request.organization,
        )

        # Enrollment check
        if not Enrollment.objects.filter(
            user=self.request.user,
            course=assessment.course,
            status=Enrollment.Status.ACTIVE,
        ).exists():
            raise PermissionDenied("Not enrolled in this course")

        # Deadline check
        if not assessment.is_open():
            raise ValidationError("Assessment is closed")

        serializer.save(
            assessment=assessment,
            student=self.request.user,
        )
