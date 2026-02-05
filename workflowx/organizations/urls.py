from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet,OrganizationMemberViewSet
from django.urls import path
router = DefaultRouter()
router.register('organizations', OrganizationViewSet, basename='organization')

urlpatterns = router.urls

member_list = OrganizationMemberViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns += [
    path(
        'organizations/<int:organization_pk>/members/',
        member_list,
        name='organization-members'
    ),
]
