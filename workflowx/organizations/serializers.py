from rest_framework import serializers
from .models import Organization, OrganizationMember

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')


class OrganizationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'name')

    def create(self, validated_data):
        user = self.context['request'].user

        org = Organization.objects.create(
            name=validated_data['name'],
            owner=user
        )

        OrganizationMember.objects.create(
            user=user,
            organization=org,
            role=OrganizationMember.OWNER
        )

        return org

class OrganizationMemberSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = OrganizationMember
        fields = (
            'id',
            'user',
            'user_email',
            'role',
            'joined_at',
        )
        read_only_fields = ('joined_at',)
