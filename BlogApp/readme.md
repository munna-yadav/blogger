

# Django Blog Project

This is a simple blog application built using Django, where users can create, edit, and delete blog posts. It also supports user authentication, allowing users to comment on posts. The project is designed with scalability and ease of use in mind, providing a clean interface for both blog authors and readers.

## Features

- User registration and authentication using `django-allauth`
- Create, edit, and delete blog posts
- Comment system for blog posts
- Responsive design with Bootstrap for mobile and desktop views
- Django Admin interface for managing users and blog posts

## Project Structure

The project is organized into two Django apps: `blog` and `BlogApp`. The `blog` app contains the models, views, and templates for the blog posts and comments. The `BlogApp` app handles user registration, authentication, and the homepage view.
```bash
├── BlogApp
│   ├── blog
│   │   ├── admin.py # register models to admin
│   │   ├── apps.py 
│   │   ├── forms.py # forms for creating and editing posts
│   │   ├── migrations # database migrations
│   │   ├── models.py # database models
│   │   ├── templates # HTML templates
│   │   ├── tests.py 
│   │   ├── urls.py # URL routing for the blog app
│   │   └── views.py # views for handling requests
│   ├── BlogApp
│   │   ├── asgi.py
│   │   ├── forms.py # forms for user registration and login
│   │   ├── __init__.py
│   │   ├── settings.py # project settings
│   │   ├── urls.py # URL routing for the entire project
│   │   ├── views.py # views for handling requests
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py # Django management script for running the server
│   ├── media
│   │   └── photos
│   ├── readme.md
│   ├── requirements.txt
│   ├── static
│   │   └── style.css
│   └── templates # base templates for the project
│       
```

## Setup Instructions

1. **Clone the repository**:
   
   ```bash
   git clone git@github.com:munna-yadav/blogger.git
   ```

2. **Create a virtual environment** and activate it:

   ```bash
   python -m venv venv
    # On Windows, use venv\Scripts\activate
   ```
   ```bash
   source venv/bin/activate
    # On Windows, use venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Database setup**:

   Update the `DATABASES` settings in `blog_project/settings.py` to match your database configuration. By default, the project is set up for PostgreSQL. Alternatively, you can use SQLite for local development.

   - Run database migrations:

     ```bash
     python manage.py migrate
     ```

5. **Create a superuser** to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the blog**:

   Open your browser and navigate to `http://127.0.0.1:8000/blog` to view the blog.

## Usage

- **Admin panel**: `http://127.0.0.1:8000/admin/` for managing posts, users, and comments.
- **Blog posts**: Logged-in users can create and edit their blog posts.
- **Comments**: Users can comment on posts using the built-in comment form.


