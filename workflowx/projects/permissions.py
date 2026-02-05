from rest_framework.permissions import BasePermission
from organizations.models import OrganizationMember


class IsProjectOwnerOrManager(BasePermission):
    """
    Allows access only to org owners or managers.
    """

    def has_object_permission(self, request, view, obj):
        return OrganizationMember.objects.filter(
            organization=obj.organization,
            user=request.user,
            role__in=['owner', 'manager'],
            is_active=True
        ).exists()
