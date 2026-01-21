from rest_framework import serializers
from .models import Assessment, Submission


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = [
            "id",
            "title",
            "description",
            "deadline",
            "max_score",
            "is_published",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = [
            "id",
            "answer",
            "score",
            "submitted_at",
        ]
        read_only_fields = ["id", "score", "submitted_at"]
