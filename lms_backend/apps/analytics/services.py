from django.db.models import Count, Avg
from apps.courses.models import Lesson
from apps.enrollments.models import Enrollment
from apps.assessments.models import Submission
from .models import LessonProgress


def get_course_progress(student, course):
    total_lessons = Lesson.objects.filter(course=course).count()

    if total_lessons == 0:
        return 0

    completed_lessons = LessonProgress.objects.filter(
        student=student,
        lesson__course=course,
        completed=True,
    ).count()

    return round((completed_lessons / total_lessons) * 100, 2)


def get_assessment_average_score(assessment):
    result = Submission.objects.filter(
        assessment=assessment,
        score__isnull=False,
    ).aggregate(avg_score=Avg("score"))
    
    return result["avg_score"]


def get_course_completion_rate(course):
    total = Enrollment.objects.filter(course=course).count()

    if total == 0:
        return 0

    completed = Enrollment.objects.filter(
        course=course,
        status=Enrollment.Status.COMPLETED,
    ).count()

    return round((completed / total) * 100, 2)
