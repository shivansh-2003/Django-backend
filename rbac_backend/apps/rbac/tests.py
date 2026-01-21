from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Department, UserDepartmentRole
from .services import user_has_role


class RbacTests(TestCase):
    def test_user_role_enforcement(self) -> None:
        user = get_user_model().objects.create_user(
            username="user1", email="user1@example.com", password="pass"
        )
        department = Department.objects.create(name="Engineering")
        UserDepartmentRole.objects.create(
            user=user, department=department, role=UserDepartmentRole.READ
        )

        self.assertTrue(user_has_role(user, department.id, UserDepartmentRole.READ))
        self.assertFalse(
            user_has_role(user, department.id, UserDepartmentRole.READ_WRITE)
        )
