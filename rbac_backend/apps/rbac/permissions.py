from functools import wraps

from django.http import HttpRequest, HttpResponseForbidden

from .models import UserDepartmentRole
from .services import user_has_role


def department_role_required(required_role: str):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request: HttpRequest, *args, **kwargs):
            department_id = request.headers.get("X-Department-ID") or request.GET.get(
                "department_id"
            )
            if not department_id:
                return HttpResponseForbidden("Department context is required.")
            if not user_has_role(request.user, department_id, required_role):
                return HttpResponseForbidden("Insufficient department role.")
            return view_func(request, *args, **kwargs)

        return _wrapped

    return decorator


class DepartmentRoleRequiredMixin:
    required_role = UserDepartmentRole.READ
    department_header = "X-Department-ID"

    def dispatch(self, request, *args, **kwargs):
        department_id = request.headers.get(self.department_header) or request.GET.get(
            "department_id"
        )
        if not department_id:
            return HttpResponseForbidden("Department context is required.")
        if not user_has_role(request.user, department_id, self.required_role):
            return HttpResponseForbidden("Insufficient department role.")
        return super().dispatch(request, *args, **kwargs)


try:
    from rest_framework.permissions import BasePermission
except ImportError:
    BasePermission = object


class DepartmentRolePermission(BasePermission):
    required_role = UserDepartmentRole.READ
    department_header = "X-Department-ID"

    def has_permission(self, request, view):
        department_id = request.headers.get(self.department_header) or request.GET.get(
            "department_id"
        )
        if not department_id:
            return False
        return user_has_role(request.user, department_id, self.required_role)
