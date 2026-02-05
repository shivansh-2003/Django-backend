# Projects App

## Purpose

Manages projects under organizations and assigns project managers.

## Models

- Project: organization, name, description, created_by, manager, is_active

## Key Endpoints

- GET /projects/ : List projects
- POST /projects/ : Create project
- GET /projects/{id}/ : Project detail
- PUT/PATCH/DELETE /projects/{id}/ : Update or delete project
- POST /projects/{id}/assign_manager/ : Assign project manager

## Permission Rules

- Only owners or managers can create projects.
- Only owners or managers can update or delete projects.
- Only owners can assign project managers.

## File Overview

- `projects/models.py`: Defines the `Project` model.
- `projects/serializers.py`: Serializers for project create and read.
- `projects/views.py`: Project ViewSet and `assign_manager` action.
- `projects/permissions.py`: Project-level permission rules.
- `projects/urls.py`: Routes project endpoints.
- `projects/admin.py`: Registers models for Django admin.
- `projects/apps.py`: App configuration.
- `projects/tests.py`: Test stubs for the app.
