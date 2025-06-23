# @https://todo-project-xi-three.vercel.app/
# Django Backend for ToDo App

This backend replaces Express + MongoDB with Django + DRF + SQLite. It provides JWT authentication (djoser + simplejwt) and user-specific task management.

## Features
- User registration, login, logout (JWT via djoser)
- Task CRUD (create, read, update, delete)
- Search (title/description), filter by status, sort by priority/due-date
- Each user sees only their own tasks
- SQLite database (easy local setup)
- CORS enabled for React frontend

## Setup

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints
- `POST /api/auth/users/` — Register
- `POST /api/auth/jwt/create/` — Login (get JWT)
- `POST /api/auth/jwt/refresh/` — Refresh JWT
- `POST /api/auth/jwt/verify/` — Verify JWT
- `GET /api/auth/users/me/` — Get current user
- `GET/POST /api/tasks/` — List/create tasks
- `GET/PUT/PATCH/DELETE /api/tasks/<id>/` — Task detail/update/delete

## Deployment
- Uses SQLite by default (easy for Railway, Render, PythonAnywhere)
- Set `DEBUG = False` and update `ALLOWED_HOSTS` for production
- Add production CORS settings as needed

---

**This backend is designed to work with the existing React frontend. Adjust frontend API URLs if needed.** 