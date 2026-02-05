from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class ActivityLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    action = models.CharField(max_length=255)
    object_type = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.action} {self.object_type}"
