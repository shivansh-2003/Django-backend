from django.contrib import admin
from .models import Organization, OrganizationMember

class OrganizationMemberInline(admin.TabularInline):
    model = OrganizationMember
    extra = 0
    autocomplete_fields = ('user',)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    inlines = (OrganizationMemberInline,)


@admin.register(OrganizationMember)
class OrganizationMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'role', 'is_active', 'joined_at')
    list_filter = ('role', 'is_active')
    search_fields = ('user__email', 'organization__name')
