# SHOWSSTOPPERS - Netflix Clone

A full-featured Netflix-like streaming platform built with Django, featuring user authentication, content browsing, and video playback capabilities.

**Live Demo:** https://showsstoppers.pythonanywhere.com/

## Features

- 🔐 User authentication (email/username + social login)
- 🎬 Movie browsing with thumbnails and carousels
- ▶️ Video playback with custom player
- 📱 Responsive design for all devices
- 👨‍💼 Admin panel for content management
- 🎨 Modern UI with Netflix-inspired design
- 🔍 Search functionality
- 📧 Email verification and notifications

## Technology Stack

- **Backend:** Django 5.2.6
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Authentication:** Django Allauth
- **Frontend:** HTML5, CSS3, JavaScript
- **Libraries:** jQuery, Owl Carousel
- **Media Processing:** Pillow

## Project Architecture

### High-Level Architecture

This is a **Django-based web application** following the **Model-View-Template (MVT)** architectural pattern. It's designed as a Netflix-like streaming platform with user authentication, content browsing, and video playback capabilities.

### Technology Stack Details

- **Backend Framework:** Django 5.2.6
- **Database:** SQLite (development), configured for PostgreSQL in production
- **Authentication:** Django Allauth (email/username + social login support)
- **Frontend:** HTML5, CSS3, JavaScript (jQuery, Owl Carousel)
- **Media Handling:** Django's built-in file handling with Pillow for image processing
- **Deployment:** WSGI/ASGI ready, static/media file serving configured

### Project Structure

```
SHOWSSTOPPERS-A-Netflix-Clone/
├── SS/                          # Main Django project
│   ├── settings.py             # Project configuration
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI entry point
│   └── asgi.py                 # ASGI entry point
├── MyApp/                      # Main application
│   ├── models.py               # Data models
│   ├── views.py                # Business logic
│   ├── admin.py                # Admin interface
│   ├── apps.py                 # App configuration
│   └── migrations/             # Database migrations
├── templates/                  # HTML templates
│   ├── index.html              # Landing page
│   ├── user_dashbord/          # User-facing pages
│   │   ├── browse.html         # Main content page
│   │   ├── play.html           # Video player
│   │   └── home.html           # Account page
│   └── account/                # Auth templates
├── static/                     # Static assets (CSS, JS, images)
└── media/                      # User-uploaded content
```

### Core Components

#### 1. **Models Layer**
- **Movie Model:** Stores movie metadata (title, description, year, rating, director, files)
- **File Handling:** ImageField for thumbnails, FileField for video files
- **Relationships:** No complex relationships currently implemented

#### 2. **Views Layer**
- **Function-based views** handling HTTP requests
- **Authentication decorators** protecting content views
- **Data fetching** from database and template rendering
- **Key views:**
  - `index`: Landing page routing
  - `movieList`: Main content browsing
  - `play_view`: Video playback
  - `dash`: User account page

#### 3. **Templates Layer**
- **Base templates** with shared components (header, footer, navigation)
- **Dynamic content** using Django template language
- **Responsive design** with CSS and JavaScript
- **Carousel implementation** using Owl Carousel for content browsing

#### 4. **URL Configuration**
- **Project-level routing** in `SS/urls.py`
- **App-level routing** (currently minimal)
- **Static/media file serving** in development

### Data Flow

```
User Request → URL Router → View Function → Model Query → Template Rendering → Response
```

1. **Authentication Flow:**
   - Unauthenticated users see landing page
   - Login redirects to content browsing
   - Allauth handles registration and social auth

2. **Content Consumption Flow:**
   - Home page displays movie grid/carousel
   - Click movie → Play page with video player
   - Admin panel for content management

### Key Design Patterns

- **MVT Architecture:** Clear separation of data, logic, and presentation
- **Decorator Pattern:** Login requirements and caching
- **Template Inheritance:** Reusable base templates
- **Static File Organization:** Centralized asset management

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd SHOWSSTOPPERS-A-Netflix-Clone-
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

7. **Run development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### For Users
1. Register/Login at the landing page
2. Browse movies on the home page
3. Click on movies to watch them
4. Access account settings from the user menu

### For Admins
1. Login to admin panel
2. Add/edit movies with thumbnails and video files
3. Manage user accounts and email addresses
4. Configure social authentication providers

## Configuration

### Environment Variables
Set these in your environment or `settings.py`:

```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
SECRET_KEY = 'your-secret-key'
```

### Social Authentication
Configure providers in `settings.py`:

```python
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
    }
}
```

## Deployment

### Production Setup
1. Set `DEBUG = False` in settings.py
2. Configure production database (PostgreSQL)
3. Set up static file serving (nginx/CDN)
4. Configure email backend
5. Use production WSGI server (Gunicorn)

### Docker (Optional)
```dockerfile
# Add Dockerfile content here
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Security & Configuration

- **Authentication:** Multi-method (email, username, social)
- **Authorization:** Login-required views
- **CSRF Protection:** Enabled by default
- **Static File Security:** Proper serving configuration
- **Environment Variables:** Email credentials (should be env vars)

## Scalability Considerations

**Current Limitations:**
- Single monolithic app (could split into micro-apps)
- SQLite database (not production-ready)
- No caching layer implemented
- No API endpoints (tight coupling between views and templates)
- Static files served by Django (should use CDN)

**Recommended Improvements:**
- Implement REST API with Django REST Framework
- Add Redis caching
- Database optimization and indexing
- CDN integration for media files
- Background task processing for uploads
- Logging and monitoring

## Support

For support, email showsstoppers23@gmail.com or create an issue in the repository.
# sciff-2025
# sciff-2025
# sciff-2025
