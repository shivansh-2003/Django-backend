from django.conf import settings
from django.db import models
from django.db.models.functions import Lower


class Department(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="children"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="created_departments",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_department_name_ci",
            )
        ]

    def __str__(self) -> str:
        return self.name


class DepartmentTable(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="tables"
    )
    name = models.CharField(max_length=200)
    schema = models.JSONField(default=dict, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="created_department_tables",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["department", "name"],
                name="unique_department_table_name",
            )
        ]
        indexes = [
            models.Index(fields=["department"]),
            models.Index(fields=["name"]),
        ]

    def __str__(self) -> str:
        return f"{self.department}::{self.name}"


class UserDepartmentRole(models.Model):
    READ = "read"
    APPEND = "append"
    ADMIN = "admin"
    ROLE_CHOICES = [
        (READ, "Read"),
        (APPEND, "Read/Append"),
        (ADMIN, "Admin"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="department_roles"
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="user_roles"
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="assigned_department_roles",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "department"],
                name="unique_user_department_role",
            )
        ]
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["department"]),
        ]

    def __str__(self) -> str:
        return f"{self.user} -> {self.department} ({self.role})"
