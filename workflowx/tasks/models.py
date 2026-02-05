from django.conf import settings
from django.db import models
from projects.models import Project

User = settings.AUTH_USER_MODEL

class Task(models.Model):

    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigned_tasks'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=TODO
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default=MEDIUM
    )
    due_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
