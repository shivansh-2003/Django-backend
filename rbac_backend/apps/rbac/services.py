from typing import Optional

from .models import UserDepartmentRole

ROLE_HIERARCHY = {
    UserDepartmentRole.READ: 1,
    UserDepartmentRole.READ_WRITE: 2,
}


def get_user_role(user, department_id) -> Optional[str]:
    if user is None or not user.is_authenticated:
        return None
    role = (
        UserDepartmentRole.objects.filter(user=user, department_id=department_id)
        .values_list("role", flat=True)
        .first()
    )
    return role


def user_has_role(user, department_id, required_role: str) -> bool:
    if user is None or not user.is_authenticated:
        return False
    role = get_user_role(user, department_id)
    if role is None:
        return False
    return ROLE_HIERARCHY.get(role, 0) >= ROLE_HIERARCHY.get(required_role, 0)
