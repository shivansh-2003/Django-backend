from django.contrib import admin

from .models import Department, DepartmentTable, UserDepartmentRole


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "created_by", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(DepartmentTable)
class DepartmentTableAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "created_by", "created_at", "updated_at")
    search_fields = ("name", "department__name")
    list_filter = ("department",)


@admin.register(UserDepartmentRole)
class UserDepartmentRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "department", "role", "assigned_by", "created_at")
    list_filter = ("role",)
    search_fields = ("user__username", "department__name")
