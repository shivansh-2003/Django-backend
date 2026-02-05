from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Organization,OrganizationMember
from .serializers import (
    OrganizationSerializer,
    OrganizationCreateSerializer,
    OrganizationMemberSerializer
    
)
from rest_framework.exceptions import PermissionDenied
from .models import OrganizationMember

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

class OrganizationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Organization.objects.filter(
            members__user=self.request.user,
            members__is_active=True
        )

    def get_serializer_class(self):
        if self.action == 'create':
            return OrganizationCreateSerializer
        return OrganizationSerializer


class OrganizationMemberViewSet(ModelViewSet):
    serializer_class = OrganizationMemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        org_id = self.kwargs['organization_pk']
        # region agent log
        _debug_log(
            {
                "sessionId": "debug-session",
                "runId": "pre-fix",
                "hypothesisId": "H4",
                "location": "organizations/views.py:OrganizationMemberViewSet.get_queryset",
                "message": "Org member list filter",
                "data": {
                    "organization_pk": org_id,
                    "has_is_active_filter": False,
                },
            }
        )
        # endregion
        return OrganizationMember.objects.filter(
            organization_id=org_id
        )

    def perform_create(self, serializer):
        org_id = self.kwargs['organization_pk']

        membership = OrganizationMember.objects.filter(
            organization_id=org_id,
            user=self.request.user,
            role__in=['owner', 'manager']
        ).exists()

        if not membership:
            raise PermissionDenied("Only owners or managers can add members")

        serializer.save(organization_id=org_id)
