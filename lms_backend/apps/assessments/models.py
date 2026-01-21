from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class Assessment(models.Model):
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="assessments",
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    deadline = models.DateTimeField()
    max_score = models.PositiveIntegerField(default=100)

    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_open(self):
        return self.is_published and timezone.now() <= self.deadline

    def __str__(self):
        return f"{self.title} ({self.course})"


class Submission(models.Model):
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    answer = models.TextField()

    score = models.PositiveIntegerField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("assessment", "student")

    def __str__(self):
        return f"{self.student} → {self.assessment}"
