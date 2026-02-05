from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Project
from .serializers import (
    ProjectSerializer,
    ProjectCreateSerializer,
)
from .permissions import IsProjectOwnerOrManager

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


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(
            organization__members__user=self.request.user,
            organization__members__is_active=True
        ).select_related('organization', 'manager')

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateSerializer
        return ProjectSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # region agent log
        _debug_log(
            {
                "sessionId": "debug-session",
                "runId": "pre-fix",
                "hypothesisId": "H3",
                "location": "projects/views.py:ProjectViewSet.perform_create",
                "message": "Project created",
                "data": {
                    "project_id": getattr(instance, "id", None),
                    "created_by_id": getattr(instance, "created_by_id", None),
                },
            }
        )
        # endregion

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), IsProjectOwnerOrManager()]
        if self.action == 'destroy':
            return [IsAuthenticated(), IsProjectOwnerOrManager()]
        return super().get_permissions()

    @action(detail=True, methods=['post'])
    def assign_manager(self, request, pk=None):
        project = self.get_object()
        new_manager_id = request.data.get('manager_id')

        is_owner = project.organization.members.filter(
            user=request.user,
            role='owner',
            is_active=True
        ).exists()

        # region agent log
        _debug_log(
            {
                "sessionId": "debug-session",
                "runId": "pre-fix",
                "hypothesisId": "H5",
                "location": "projects/views.py:ProjectViewSet.assign_manager",
                "message": "Assign manager attempt",
                "data": {
                    "project_id": getattr(project, "id", None),
                    "new_manager_id": new_manager_id,
                    "is_owner": is_owner,
                },
            }
        )
        # endregion

        if not is_owner:
            raise PermissionDenied("Only owners can assign managers")

        project.manager_id = new_manager_id
        project.save()

        return Response({"status": "manager assigned"})
