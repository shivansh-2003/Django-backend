from rest_framework.permissions import BasePermission
from apps.organizations.models import OrganizationMember


class CanManageEnrollments(BasePermission):
    def has_permission(self, request, view):
        membership = OrganizationMember.objects.filter(
            user=request.user,
            organization=request.organization,
            is_active=True,
        ).first()

        if not membership:
            return False

        return membership.role in ("ADMIN", "INSTRUCTOR")
