from django.contrib import admin
from .models import ActivityLog

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'object_type', 'object_id', 'timestamp')
    list_filter = ('object_type', 'timestamp')
    search_fields = ('action',)

    readonly_fields = (
        'user',
        'action',
        'object_type',
        'object_id',
        'timestamp',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
