from django.contrib import admin

from .models import Department, UserDepartmentRole


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(UserDepartmentRole)
class UserDepartmentRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "department", "role", "assigned_by", "created_at")
    list_filter = ("role",)
    search_fields = ("user__username", "department__name")
