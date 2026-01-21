from django.utils.deprecation import MiddlewareMixin

from .models import Department


class DepartmentContextMiddleware(MiddlewareMixin):
    def process_request(self, request):
        department_id = request.headers.get("X-Department-ID") or request.GET.get(
            "department_id"
        )
        request.department_id = department_id
        request.department = None
        if not department_id:
            return None
        try:
            request.department = Department.objects.get(id=department_id)
        except (Department.DoesNotExist, ValueError):
            request.department = None
        return None
