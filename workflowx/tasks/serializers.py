from rest_framework import serializers
from .models import Task

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


class TaskSerializer(serializers.ModelSerializer):
    assigned_to_email = serializers.EmailField(
        source='assigned_to.email',
        read_only=True
    )

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'project',
            'assigned_to',
            'assigned_to_email',
            'status',
            'priority',
            'due_date',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')


from organizations.models import OrganizationMember

class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'id',
            'project',
            'title',
            'description',
            'assigned_to',
            'priority',
            'due_date',
        )

    def validate(self, attrs):
        user = self.context['request'].user
        project = attrs['project']
        # region agent log
        _debug_log(
            {
                "sessionId": "debug-session",
                "runId": "pre-fix",
                "hypothesisId": "H3",
                "location": "tasks/serializers.py:TaskCreateSerializer.validate",
                "message": "Task create validate",
                "data": {
                    "user_id": getattr(user, "id", None),
                    "attrs_keys": sorted(list(attrs.keys())),
                },
            }
        )
        # endregion

        membership = OrganizationMember.objects.filter(
            organization=project.organization,
            user=user,
            role__in=['owner', 'manager'],
            is_active=True
        ).exists()

        if not membership:
            raise serializers.ValidationError(
                "Only owners or managers can create tasks"
            )

        return attrs
