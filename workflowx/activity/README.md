# Activity App

## Purpose

Stores activity logs for auditing and history tracking.

## Models

- ActivityLog: user, action, object_type, object_id, timestamp

## Notes

- API endpoints are not implemented yet.
- Intended for recording actions like create/update/delete across the system.

## File Overview

- `activity/models.py`: Defines the `ActivityLog` model.
- `activity/views.py`: Placeholder views for future activity endpoints.
- `activity/urls.py`: URL configuration (currently empty).
- `activity/admin.py`: Registers models for Django admin.
- `activity/apps.py`: App configuration.
- `activity/tests.py`: Test stubs for the app.
