#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    # region agent log
    import json
    import time

    def _debug_log(payload):
        payload.setdefault("timestamp", int(time.time() * 1000))
        with open(
            "/Users/shivanshmahajan/Developer/django/.cursor/debug.log", "a"
        ) as _log_file:
            _log_file.write(json.dumps(payload) + "\n")

    _debug_log(
        {
            "sessionId": "debug-session",
            "runId": "pre-fix",
            "hypothesisId": "H0",
            "location": "manage.py:main",
            "message": "manage.py invoked",
            "data": {
                "cwd": os.getcwd(),
                "argv": sys.argv,
                "settings_module": os.environ.get("DJANGO_SETTINGS_MODULE"),
            },
        }
    )
    # endregion
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
