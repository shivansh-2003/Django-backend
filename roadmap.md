# Django + DRF Roadmap To‑Do

Use this checklist to track progress in order.

## 1. Python and Web Basics

- [ ] Python: data types, functions, OOP, modules, virtualenv, packaging. [coursera](https://www.coursera.org/resources/django-learning-roadmap)
- [ ] Web fundamentals: HTTP methods, status codes, JSON, HTML/CSS basics, basic JavaScript. [youtube](https://www.youtube.com/watch?v=lLewD9pqtjM)

## 2. Core Django Fundamentals

- [x] Django project/app structure, `manage.py`, `settings.py`, `urls.py`. [youtube](https://www.youtube.com/watch?v=lLewD9pqtjM)
- [x] Views (function‑based), URL routing, request/response cycle. [youtube](https://www.youtube.com/watch?v=Rp5vd34d-z4)
- [ ] Templates: template language, tags, filters, static files. [youtube](https://www.youtube.com/watch?v=lLewD9pqtjM)
- [x] Models and ORM: fields, relationships, migrations, querying. [youtube](https://www.youtube.com/watch?v=Rp5vd34d-z4)
- [ ] Admin site: registering models, basic customization. [youtube](https://www.youtube.com/watch?v=lLewD9pqtjM)

## 3. Intermediate Django (Production‑Ready Web App)

- [ ] Forms & ModelForms, validation, CSRF, handling file uploads. [linkedin](https://www.linkedin.com/posts/p-phanindra-ratna-gopi-706b352aa_django-2025-complete-roadmap-activity-7333060245260222464-tUlW)
- [ ] Class‑based views and generic views (ListView, DetailView, Create/Update/DeleteView). [youtube](https://www.youtube.com/watch?v=UkkFTTVytmU)
- [ ] Authentication & authorization: users, sessions, login/logout, groups, permissions. [youtube](https://www.youtube.com/watch?v=LBXXxXMbY5I)
- [ ] Advanced ORM: select_related/prefetch_related, annotations, aggregations, performance basics. [coursera](https://www.coursera.org/resources/django-learning-roadmap)
- [ ] Project structure & config: multiple settings (dev/prod), environment variables, secrets. [karmickinstitute](https://www.karmickinstitute.com/resources/python-django-developer-career-scope-roadmap-2025/)

## 4. Core DRF Fundamentals

- [x] DRF setup and configuration in an existing Django project. [github](https://github.com/analyticalnahid/django_rest_roadmap)
- [x] What is REST, RESTful resource design, versioned API endpoints. [testdriven](https://testdriven.io/blog/drf-basics/)
- [x] Serializers vs `ModelSerializer`, validation, create/update hooks, nested serializers basics. [youtube](https://www.youtube.com/watch?v=8d1HgJTEGe8)
- [x] Function‑based API views with `@api_view`. [testdriven](https://testdriven.io/blog/drf-basics/)
- [x] Class‑based `APIView`. [youtube](https://www.youtube.com/watch?v=8d1HgJTEGe8)
- [ ] Mixins and generic API views (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`). [testdriven](https://testdriven.io/blog/drf-basics/)
- [ ] ViewSets and `ModelViewSet`, custom actions, routers. [youtube](https://www.youtube.com/watch?v=8d1HgJTEGe8)
- [ ] Browsable API & using Postman/HTTP clients for testing. [youtube](https://www.youtube.com/watch?v=8d1HgJTEGe8)

## 5. Robust API Features (Must‑Have for Jobs)

- [ ] Authentication: session auth, token auth, JWT (e.g., SimpleJWT). [geekyshows](https://geekyshows.com/course/django-res/)
- [ ] Permissions: built‑in classes, custom permission classes, role‑based access. [geekyshows](https://geekyshows.com/course/django-res/)
- [ ] Pagination: global and per‑view, custom pagination classes. [testdriven](https://testdriven.io/blog/drf-basics/)
- [ ] Filtering, search, ordering: `DjangoFilterBackend`, `SearchFilter`, `OrderingFilter`. [testdriven](https://testdriven.io/blog/drf-basics/)
- [ ] Throttling / rate limiting. [geekyshows](https://geekyshows.com/course/django-res/)
- [ ] Advanced validation: custom validators, field‑level and object‑level validation. [geekyshows](https://geekyshows.com/course/django-res/)
- [ ] Error handling & response patterns (consistent error schema, DRF exceptions). [github](https://github.com/analyticalnahid/django_rest_roadmap)

## 6. Advanced Django + DRF Patterns

- [ ] Advanced serializers: nested, writable nested, custom fields, HyperlinkedModelSerializer. [github](https://github.com/analyticalnahid/django_rest_roadmap)
- [ ] Content negotiation, custom renderers/parsers (e.g., CSV, custom JSON). [github](https://github.com/analyticalnahid/django_rest_roadmap)
- [ ] Signals, middleware, custom management commands for API‑related workflows. [linkedin](https://www.linkedin.com/posts/p-phanindra-ratna-gopi-706b352aa_django-2025-complete-roadmap-activity-7333060245260222464-tUlW)
- [ ] Async Django: async views, when to use them. [youtube](https://www.youtube.com/watch?v=1J47P9ZuhTU)
- [ ] Real‑time features: Django Channels, WebSockets integrations with APIs. [youtube](https://www.youtube.com/watch?v=LBXXxXMbY5I)
- [ ] Pattern choices: when to use FBV/CBV/Generic/ViewSet, modular app design. [reddit](https://www.reddit.com/r/django/comments/1pcea5g/need_a_clean_django_drf_deployment_roadmap_free/)

## 7. Ecosystem for Job‑Ready Backend

- [ ] Background tasks: Celery with Redis/RabbitMQ (task queues, scheduled jobs). [youtube](https://www.youtube.com/watch?v=LBXXxXMbY5I)
- [ ] Caching: per‑view, low‑level, Redis cache, cache invalidation strategies. [karmickinstitute](https://www.karmickinstitute.com/resources/python-django-developer-career-scope-roadmap-2025/)
- [ ] Search: integrating Elasticsearch or similar with Django/DRF. [linkedin](https://www.linkedin.com/posts/p-phanindra-ratna-gopi-706b352aa_django-2025-complete-roadmap-activity-7333060245260222464-tUlW)
- [ ] File storage: media on S3/Cloud, signed URLs. [karmickinstitute](https://www.karmickinstitute.com/resources/python-django-developer-career-scope-roadmap-2025/)
- [ ] Logging and monitoring: Django logging config, Sentry or similar. [linkedin](https://www.linkedin.com/posts/p-phanindra-ratna-gopi-706b352aa_django-2025-complete-roadmap-activity-7333060245260222464-tUlW)

## 8. Deployment and DevOps

- [ ] Dockerizing Django + DRF app (Dockerfile, docker‑compose). [karmickinstitute](https://www.karmickinstitute.com/resources/python-django-developer-career-scope-roadmap-2025/)
- [ ] Production stack: Nginx + Gunicorn/Uvicorn, static/media serving. [karmickinstitute](https://www.karmickinstitute.com/resources/python-django-developer-career-scope-roadmap-2025/)
- [ ] Using environment variables, `.env`, secrets in production. [linkedin](https://www.linkedin.com/posts/p-phanindra-ratna-gopi-706b352aa_django-2025-complete-roadmap-activity-7333060245260222464-tUlW)
- [ ] Deploying to a cloud provider (AWS, DigitalOcean, Render, etc.). [linkedin](https://www.linkedin.com/posts/p-phanindra-ratna-gopi-706b352aa_django-2025-complete-roadmap-activity-7333060245260222464-tUlW)
- [ ] CI/CD basics: automated tests, linting, build & deploy pipeline. [karmickinstitute](https://www.karmickinstitute.com/resources/python-django-developer-career-scope-roadmap-2025/)
