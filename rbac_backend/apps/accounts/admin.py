from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Security", {"fields": ("last_login_ip",)}),
    )
    list_display = UserAdmin.list_display + ("last_login_ip",)
