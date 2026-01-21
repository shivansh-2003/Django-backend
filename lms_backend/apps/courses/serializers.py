from rest_framework import serializers
from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "is_published",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "title",
            "content",
            "order",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
