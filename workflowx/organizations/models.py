from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Organization(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owned_organizations'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class OrganizationMember(models.Model):

    OWNER = 'owner'
    MANAGER = 'manager'
    MEMBER = 'member'

    ROLE_CHOICES = [
        (OWNER, 'Owner'),
        (MANAGER, 'Manager'),
        (MEMBER, 'Member'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='organization_memberships'
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='members'
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user} → {self.organization} ({self.role})"
