from rest_framework import serializers
from .models import Project

# region agent log
import json
import time

def _debug_log(payload):
    payload.setdefault("timestamp", int(time.time() * 1000))
    with open(
        "/Users/shivanshmahajan/Developer/django/.cursor/debug.log", "a"
    ) as _log_file:
        _log_file.write(json.dumps(payload) + "\n")
# endregion


class ProjectSerializer(serializers.ModelSerializer):
    manager_email = serializers.EmailField(
        source='manager.email',
        read_only=True
    )

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
            'organization',
            'manager',
            'manager_email',
            'is_active',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')


class ProjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
            'organization',
            'manager',
        )

    def validate(self, attrs):
        user = self.context['request'].user
        org = attrs['organization']
        # region agent log
        _debug_log(
            {
                "sessionId": "debug-session",
                "runId": "pre-fix",
                "hypothesisId": "H3",
                "location": "projects/serializers.py:ProjectCreateSerializer.validate",
                "message": "Project create validate",
                "data": {
                    "user_id": getattr(user, "id", None),
                    "attrs_keys": sorted(list(attrs.keys())),
                },
            }
        )
        # endregion

        is_allowed = org.members.filter(
            user=user,
            role__in=['owner', 'manager'],
            is_active=True
        ).exists()

        if not is_allowed:
            raise serializers.ValidationError(
                "You are not allowed to create projects in this organization"
            )

        return attrs
