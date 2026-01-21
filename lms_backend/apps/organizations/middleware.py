from django.http import JsonResponse
from .models import Organization, OrganizationMember


class OrganizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip for admin & auth endpoints
        if request.path.startswith("/admin") or request.path.startswith("/api/auth"):
            return self.get_response(request)

        org_id = request.headers.get("X-ORG-ID")

        if not org_id:
            return JsonResponse(
                {"detail": "X-ORG-ID header missing"},
                status=400
            )

        try:
            organization = Organization.objects.get(id=org_id, is_active=True)
        except Organization.DoesNotExist:
            return JsonResponse(
                {"detail": "Invalid organization"},
                status=404
            )

        if not request.user.is_authenticated:
            return JsonResponse(
                {"detail": "Authentication required"},
                status=401
            )

        is_member = OrganizationMember.objects.filter(
            user=request.user,
            organization=organization,
            is_active=True,
        ).exists()

        if not is_member:
            return JsonResponse(
                {"detail": "Not a member of this organization"},
                status=403
            )

        # Attach org to request
        request.organization = organization

        return self.get_response(request)
