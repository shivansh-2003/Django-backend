from rest_framework import serializers
from .models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            "id",
            "user",
            "course",
            "status",
            "enrolled_at",
            "completed_at",
        ]
        read_only_fields = ["id", "enrolled_at", "completed_at"]
