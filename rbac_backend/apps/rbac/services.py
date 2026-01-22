from typing import Optional

from .models import UserDepartmentRole

ROLE_HIERARCHY = {
    UserDepartmentRole.READ: 1,
    UserDepartmentRole.APPEND: 2,
    UserDepartmentRole.ADMIN: 3,
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


def is_super_admin(user) -> bool:
    return bool(user and user.is_authenticated and getattr(user, "is_super_admin", False))


def user_has_role(user, department_id, required_role: str) -> bool:
    if user is None or not user.is_authenticated:
        return False
    if is_super_admin(user):
        return True
    role = get_user_role(user, department_id)
    if role is None:
        return False
    return ROLE_HIERARCHY.get(role, 0) >= ROLE_HIERARCHY.get(required_role, 0)


def user_can_read(user, department_id) -> bool:
    return user_has_role(user, department_id, UserDepartmentRole.READ)


def user_can_append(user, department_id) -> bool:
    return user_has_role(user, department_id, UserDepartmentRole.APPEND)


def user_is_department_admin(user, department_id) -> bool:
    return user_has_role(user, department_id, UserDepartmentRole.ADMIN)


def user_can_manage_departments(user) -> bool:
    return is_super_admin(user)
