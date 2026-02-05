# Tasks App

## Purpose

Manages tasks within projects, including assignment, status, and priority.

## Models

- Task: project, title, description, assigned_to, status, priority, due_date

## Key Endpoints

- GET /tasks/ : List tasks
- POST /tasks/ : Create task
- GET /tasks/{id}/ : Task detail
- PUT/PATCH/DELETE /tasks/{id}/ : Update or delete task

## Task Query Options

- Filter: `?status=todo&priority=high&assigned_to=3`
- Search: `?search=keyword`
- Ordering: `?ordering=due_date` or `?ordering=-created_at`

## Permission Rules

- Any active org member can view tasks.
- Owners and managers can modify any task.
- Members can modify only tasks assigned to them.

## File Overview

- `tasks/models.py`: Defines the `Task` model and status/priority choices.
- `tasks/serializers.py`: Serializers for task create and read.
- `tasks/views.py`: Task ViewSet with filtering, search, and ordering.
- `tasks/permissions.py`: Task-level permission rules.
- `tasks/urls.py`: Routes task endpoints.
- `tasks/admin.py`: Registers models for Django admin.
- `tasks/apps.py`: App configuration.
- `tasks/tests.py`: Test stubs for the app.
