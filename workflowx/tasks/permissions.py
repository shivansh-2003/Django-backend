from rest_framework.permissions import BasePermission
from organizations.models import OrganizationMember


class CanAccessTask(BasePermission):
    """
    View permission: any active org member
    """

    def has_object_permission(self, request, view, obj):
        return OrganizationMember.objects.filter(
            organization=obj.project.organization,
            user=request.user,
            is_active=True
        ).exists()


class CanModifyTask(BasePermission):
    """
    Modify permission:
    - Owner / Manager → any task
    - Member → only own task
    """

    def has_object_permission(self, request, view, obj):
        membership = OrganizationMember.objects.filter(
            organization=obj.project.organization,
            user=request.user,
            is_active=True
        ).first()

        if not membership:
            return False

        if membership.role in ['owner', 'manager']:
            return True

        return obj.assigned_to == request.user
