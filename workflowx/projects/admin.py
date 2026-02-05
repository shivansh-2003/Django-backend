from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'organization',
        'manager',
        'is_active',
        'created_at'
    )
    list_filter = ('is_active', 'organization')
    search_fields = ('name',)
    autocomplete_fields = ('organization', 'manager', 'created_by')
