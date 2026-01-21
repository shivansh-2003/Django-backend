from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Organization(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="owned_organizations",
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrganizationMember(models.Model):
    class OrgRole(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        INSTRUCTOR = "INSTRUCTOR", "Instructor"
        STUDENT = "STUDENT", "Student"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="organization_memberships",
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="members",
    )

    role = models.CharField(
        max_length=20,
        choices=OrgRole.choices,
    )

    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "organization")

    def __str__(self):
        return f"{self.user} → {self.organization} ({self.role})"
