from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer
from .permissions import CanAccessTask, CanModifyTask

# region agent log
import json
import time

def _debug_log(payload):
    payload.setdefault("timestamp", int(time.time() * 1000))
    with open(
        "/Users/shivanshmahajan/Developer/django/.cursor/debug.log", "a"
    ) as _log_file:
        _log_file.write(json.dumps(payload) + "\n")
# endregion


class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    filterset_fields = ['status', 'priority', 'assigned_to']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'priority', 'created_at']

    def get_queryset(self):
        return Task.objects.filter(
            project__organization__members__user=self.request.user,
            project__organization__members__is_active=True
        ).select_related(
            'project',
            'assigned_to',
            'project__organization'
        )

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # region agent log
        _debug_log(
            {
                "sessionId": "debug-session",
                "runId": "pre-fix",
                "hypothesisId": "H3",
                "location": "tasks/views.py:TaskViewSet.perform_create",
                "message": "Task created",
                "data": {
                    "task_id": getattr(instance, "id", None),
                    "created_by_id": getattr(instance, "created_by_id", None),
                },
            }
        )
        # endregion

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            return [IsAuthenticated(), CanAccessTask()]

        if self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), CanModifyTask()]

        if self.action == 'destroy':
            return [IsAuthenticated(), CanModifyTask()]

        return super().get_permissions()
