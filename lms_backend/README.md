# Multi-Tenant Learning Management System (LMS) Backend

A production-grade, multi-tenant Learning Management System backend built with Django and Django REST Framework. This project demonstrates professional backend architecture, security best practices, and scalable design patterns.

## 🎯 Project Overview

This LMS backend provides a complete API-only system for managing:
- **Organizations** (Multi-tenant isolation)
- **Users & Roles** (Custom authentication system)
- **Courses & Lessons** (Content management)
- **Enrollments** (Student-course relationships)
- **Assessments & Submissions** (Evaluation system)
- **Analytics** (Progress tracking & reporting)

## 🏗️ Architecture Highlights

### Modular Monolith Design
- **6 Feature-Based Apps**: Each app has a single, clear responsibility
- **Clean Separation**: Business logic separated from configuration
- **Scalable Structure**: Easy to extend and maintain

### Multi-Tenancy
- **Organization-Based Isolation**: All data scoped by organization
- **Middleware-Enforced Security**: Centralized tenant validation
- **Role-Per-Context**: Users can have different roles in different orgs

### Security First
- **JWT Authentication**: Stateless, scalable auth system
- **Server-Side Enforcement**: No trust in client-side validation
- **Query-Level Filtering**: Database-enforced access control
- **Permission Classes**: Role-based API access

## 📁 Project Structure

```
lms_backend/
├── config/                 # Project configuration
│   ├── settings.py        # Django settings with DRF & JWT config
│   └── urls.py           # Main URL routing
├── apps/                  # Business logic apps
│   ├── accounts/         # Custom User model & authentication
│   ├── organizations/    # Multi-tenancy & organization management
│   ├── courses/         # Courses & lessons (CRUD + permissions)
│   ├── enrollments/     # Student enrollments & access control
│   ├── assessments/     # Assessments, submissions & deadlines
│   └── analytics/        # Progress tracking & analytics services
├── manage.py
├── requirements.txt
└── run.md                # Detailed setup and usage guide
```

## 🚀 Quick Start

See `run.md` for detailed setup instructions.

### Basic Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## 🔑 Key Features

### 1. Custom User Model
- Email-based authentication (no username)
- Role system (SUPER_ADMIN, ORG_ADMIN, INSTRUCTOR, STUDENT)
- Created before first migration (prevents future issues)

### 2. Multi-Tenant Architecture
- Organization middleware validates every request
- `X-ORG-ID` header required for API calls
- Automatic data isolation at query level

### 3. Role-Based Access Control
- Global roles (user identity)
- Organization roles (context-specific permissions)
- Permission classes enforce API access

### 4. Secure CRUD Operations
- Organization injected server-side (never from client)
- Queryset filtering by organization
- Students only see enrolled courses

### 5. Business Logic in Models
- Deadline enforcement in Assessment model
- Submission uniqueness at DB level
- Enrollment status lifecycle

### 6. Analytics & Progress Tracking
- Service layer for computed metrics
- ORM aggregation (Count, Avg)
- Course completion tracking

## 📡 API Endpoints

### Authentication
- `POST /api/auth/login/` - Get JWT tokens
- `POST /api/auth/refresh/` - Refresh access token

### Courses
- `GET /api/courses/` - List courses (org-filtered)
- `POST /api/courses/` - Create course (Instructor/Admin)
- `GET /api/courses/{id}/lessons/` - List lessons

### Enrollments
- `GET /api/enrollments/` - List enrollments
- `POST /api/enrollments/` - Create enrollment (Admin/Instructor)

### Assessments
- `GET /api/courses/{id}/assessments/` - List assessments
- `POST /api/assessments/{id}/submit/` - Submit assessment (Students)

### Analytics
- `GET /api/courses/{id}/analytics/` - Course analytics
- `GET /api/courses/{id}/progress/` - Student progress

## 🔐 Authentication Flow

1. **Login**: `POST /api/auth/login/` with email/password
2. **Get Tokens**: Receive `access` and `refresh` tokens
3. **API Calls**: Include `Authorization: Bearer <token>` header
4. **Organization**: Include `X-ORG-ID: <org_id>` header

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Professional Django project structure
- ✅ Multi-tenant SaaS architecture
- ✅ Custom authentication systems
- ✅ Role-based permissions
- ✅ Secure API design
- ✅ Business logic organization
- ✅ ORM optimization techniques
- ✅ Service layer patterns

## 📚 Technologies Used

- **Django 6.0** - Web framework
- **Django REST Framework** - API framework
- **djangorestframework-simplejwt** - JWT authentication
- **python-dotenv** - Environment variable management
- **SQLite** - Database (development)

## 🧪 Testing

The project is structured for easy testing:
- Models have proper constraints
- Views are thin and testable
- Services are isolated
- Permissions are explicit

## 📖 Documentation

- **run.md** - Complete setup and usage guide
- **context.txt** - Detailed learning explanations (why-first approach)

## 🎯 Next Steps

### Production Readiness
- [ ] Add PostgreSQL database
- [ ] Environment-specific settings
- [ ] Comprehensive test suite
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Rate limiting & throttling
- [ ] Logging & monitoring
- [ ] CI/CD pipeline

### Feature Enhancements
- [ ] File uploads for course materials
- [ ] Real-time notifications
- [ ] Advanced analytics dashboard
- [ ] Certificate generation
- [ ] Discussion forums
- [ ] Video integration

## 🤝 Contributing

This is a learning project. Feel free to:
- Add features
- Improve documentation
- Fix bugs
- Optimize queries

## 📝 License

This project is for educational purposes.

---

**Built with Django 6.0 and Django REST Framework**

For detailed setup instructions, see `run.md`.
