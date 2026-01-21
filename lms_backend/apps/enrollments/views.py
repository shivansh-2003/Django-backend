from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Enrollment
from .serializers import EnrollmentSerializer
from .permissions import CanManageEnrollments


class EnrollmentViewSet(ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, CanManageEnrollments]

    def get_queryset(self):
        return Enrollment.objects.filter(
            course__organization=self.request.organization
        ).select_related("user", "course")

    def perform_create(self, serializer):
        serializer.save()
