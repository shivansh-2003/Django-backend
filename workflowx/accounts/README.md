# Accounts App

## Purpose

Provides authentication and user profile endpoints. Uses a custom user model with unique email.

## Models

- User: extends Django AbstractUser with unique email.

## Key Endpoints

- POST /auth/login/ : JWT login
- POST /auth/refresh/ : Refresh access token
- GET /users/me/ : Current user profile

## Notes

- Authentication is JWT-based.
- The custom user model is defined in `accounts/models.py`.

## File Overview

- `accounts/models.py`: Defines the custom `User` model with unique email.
- `accounts/serializers.py`: Serializes user data for API responses.
- `accounts/views.py`: Implements `MeAPIView` for current user info.
- `accounts/urls.py`: Routes auth and user profile endpoints.
- `accounts/admin.py`: Registers models for Django admin.
- `accounts/apps.py`: App configuration.
- `accounts/tests.py`: Test stubs for the app.
