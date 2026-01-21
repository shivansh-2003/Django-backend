# LMS Backend - Setup and Running Guide

## Overview
This is a multi-tenant Learning Management System (LMS) backend built with Django and Django REST Framework. It provides a complete API-only backend for managing organizations, courses, enrollments, assessments, and analytics.

## Prerequisites
- Python 3.10 or higher
- pip
- virtualenv (recommended)

## Project Structure
```
lms_backend/
├── config/              # Project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py         # Main URL routing
│   └── ...
├── apps/                # Business logic apps
│   ├── accounts/       # Custom User model & authentication
│   ├── organizations/  # Multi-tenancy & organization management
│   ├── courses/        # Courses & lessons
│   ├── enrollments/    # Student enrollments
│   ├── assessments/    # Assessments & submissions
│   └── analytics/      # Progress tracking & analytics
├── manage.py
├── requirements.txt
└── run.md
```

## Installation Steps

### 1. Navigate to Project Directory
```bash
cd lms_backend
```

### 2. Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root (if not exists):
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run Migrations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts. Use an email address (not username) as per the custom User model.

### 7. Run Development Server
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication
- **POST** `/api/auth/login/` - Obtain JWT tokens (email + password)
- **POST** `/api/auth/refresh/` - Refresh access token

### Courses
- **GET** `/api/courses/` - List courses (filtered by organization)
- **POST** `/api/courses/` - Create course (Instructor/Admin only)
- **GET** `/api/courses/{id}/` - Get course details
- **PUT/PATCH** `/api/courses/{id}/` - Update course
- **DELETE** `/api/courses/{id}/` - Delete course
- **GET** `/api/courses/{course_id}/lessons/` - List lessons for a course
- **POST** `/api/courses/{course_id}/lessons/` - Create lesson

### Enrollments
- **GET** `/api/enrollments/` - List enrollments
- **POST** `/api/enrollments/` - Create enrollment (Admin/Instructor only)
- **GET** `/api/enrollments/{id}/` - Get enrollment details
- **PUT/PATCH** `/api/enrollments/{id}/` - Update enrollment
- **DELETE** `/api/enrollments/{id}/` - Delete enrollment

### Assessments
- **GET** `/api/courses/{course_id}/assessments/` - List assessments
- **POST** `/api/courses/{course_id}/assessments/` - Create assessment (Instructor/Admin only)
- **GET** `/api/assessments/{assessment_id}/submit/` - List submissions
- **POST** `/api/assessments/{assessment_id}/submit/` - Submit assessment (Students only)

### Analytics
- **GET** `/api/courses/{course_id}/analytics/` - Get course analytics
- **GET** `/api/courses/{course_id}/progress/` - Get student progress

## Authentication Flow

### 1. Login
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'
```

Response:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 2. Use Access Token
Include the token in the Authorization header:
```bash
curl -X GET http://127.0.0.1:8000/api/courses/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "X-ORG-ID: 1"
```

## Multi-Tenancy

### Organization Context
All API requests (except auth endpoints) require:
1. **JWT Authentication** - `Authorization: Bearer <token>`
2. **Organization Header** - `X-ORG-ID: <organization_id>`

The middleware validates:
- User is authenticated
- Organization exists and is active
- User is a member of the organization

### Example Request Flow
```
1. User logs in → Gets JWT token
2. User makes API request with:
   - Authorization: Bearer <token>
   - X-ORG-ID: <org_id>
3. Middleware validates membership
4. request.organization is set
5. Views filter data by organization
```

## User Roles

### Global Roles (User.role)
- `SUPER_ADMIN` - Platform-level admin
- `ORG_ADMIN` - Organization admin
- `INSTRUCTOR` - Course instructor
- `STUDENT` - Student user

### Organization Roles (OrganizationMember.role)
- `ADMIN` - Organization admin
- `INSTRUCTOR` - Instructor in organization
- `STUDENT` - Student in organization

**Note**: A user can have different roles in different organizations.

## Access Control

### Course Access
- **Instructors/Admins**: Can see all courses in their organization
- **Students**: Can only see courses they are enrolled in

### Lesson Access
- Lessons inherit course access rules
- Students can only access lessons from enrolled courses

### Assessment Access
- **Instructors/Admins**: Can create and manage assessments
- **Students**: Can view and submit assessments (if enrolled)
- Submissions are locked after deadline

## Database Models

### Core Models
- **User** - Custom user model (email-based)
- **Organization** - Tenant/Organization
- **OrganizationMember** - User ↔ Organization relationship
- **Course** - Course content
- **Lesson** - Lesson content (belongs to Course)
- **Enrollment** - Student ↔ Course relationship
- **Assessment** - Assessment/Assignment
- **Submission** - Student submission
- **LessonProgress** - Track lesson completion

## Testing the API

### Using curl
```bash
# 1. Login
TOKEN=$(curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"password"}' \
  | jq -r '.access')

# 2. List courses
curl http://127.0.0.1:8000/api/courses/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "X-ORG-ID: 1"
```

### Using Django Admin
1. Visit `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials
3. Manage all models through admin interface

## Common Tasks

### Create an Organization
1. Login to admin panel
2. Go to Organizations → Add Organization
3. Fill in name, slug, and owner
4. Note the organization ID

### Add Users to Organization
1. Go to Organization Members → Add
2. Select user and organization
3. Assign role (ADMIN, INSTRUCTOR, or STUDENT)

### Create a Course
1. Use API: `POST /api/courses/`
2. Include `X-ORG-ID` header
3. Must be authenticated as Instructor/Admin

### Enroll a Student
1. Use API: `POST /api/enrollments/`
2. Include `user` and `course` IDs
3. Must be authenticated as Instructor/Admin

## Troubleshooting

### Import Errors
If you see `ModuleNotFoundError: No module named 'organizations'`:
- Ensure imports use `apps.` prefix: `from apps.organizations.models import ...`

### Organization Middleware Errors
- Ensure `X-ORG-ID` header is included in requests
- Verify user is a member of the organization
- Check organization is active

### Permission Denied
- Verify user role in organization
- Check enrollment status for student access
- Ensure assessment deadline hasn't passed

### Migration Issues
- Run `python manage.py makemigrations` for each app
- Then `python manage.py migrate`
- If issues persist, delete `db.sqlite3` and re-run migrations

## Development Notes

### Why This Architecture?
- **Modular Monolith**: Separate apps for clear responsibilities
- **Multi-Tenancy**: Organization-based data isolation
- **Security First**: Server-side enforcement, no client trust
- **Scalable**: Query optimization, proper indexing
- **Professional**: Follows Django/DRF best practices

### Key Design Decisions
1. Custom User model from day one (prevents migration issues)
2. Organization middleware (centralized tenant isolation)
3. Role-based permissions (flexible access control)
4. Service layer for analytics (separation of concerns)
5. Fat models, thin views (business logic in models)

## Next Steps

### Production Readiness
- [ ] Add environment-specific settings (dev/prod)
- [ ] Set up proper logging
- [ ] Add API throttling
- [ ] Implement caching
- [ ] Add comprehensive tests
- [ ] Set up CI/CD
- [ ] Configure production database (PostgreSQL)
- [ ] Add API documentation (Swagger/OpenAPI)

### Feature Enhancements
- [ ] File uploads for course materials
- [ ] Real-time notifications
- [ ] Advanced analytics dashboard
- [ ] Certificate generation
- [ ] Discussion forums
- [ ] Video integration

## Support

For issues or questions:
1. Check Django/DRF documentation
2. Review the context.txt file for detailed explanations
3. Check Django admin for data verification

---

**Built with Django 6.0 and Django REST Framework**
