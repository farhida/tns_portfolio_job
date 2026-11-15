# Name_ID_Portfolio — Django Personal Portfolio

A complete Django portfolio starter based on the supplied specification sheet.

## Features

- Responsive personal portfolio home page with About, Skills, Projects, Experience and Education sections.
- Django models for profile, skills, education, experience, projects and contact messages.
- Registration with username, email, password and confirm password.
- Login and logout.
- Django contact form; submitted messages are stored in the database.
- Staff-only dashboard and Django Admin content management.
- Resume/CV page generated from database records, with browser Print / Save as PDF.
- Sample starter content command.

## Requirements

- Python 3.10+
- Django 5.2

## Setup (Windows)

Open a terminal in the project folder:

```bash
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
py manage.py makemigrations Portfolio
py manage.py migrate
py manage.py seed_portfolio
py manage.py createsuperuser
py manage.py runserver
```

Open http://127.0.0.1:8000/

## Admin login

Create a staff account with `py manage.py createsuperuser` during setup. The seed command does not create an account with a shared default password.

Admin panel: http://127.0.0.1:8000/admin/

For deployment, set a persistent `DJANGO_SECRET_KEY`, configure `DEBUG=False` and `ALLOWED_HOSTS`, and use a production-ready web server. If no key is configured, a random key is generated for local development. The public registration form creates a normal user, not a staff/admin user.

## Add your own information

1. Sign in to `/admin/`.
2. Open **Portfolio profile** and update the name, headline, biography, email, phone, location, social links and optional profile photo/resume file.
3. Add Skills, Education, Experience and Projects.
4. Open `/` to see the updated portfolio.
5. Open `/resume/` to preview the CV and choose **Print / Save PDF**.

## Main URLs

| URL | Purpose |
| --- | --- |
| `/` | Public portfolio |
| `/projects/<slug>/` | Project details |
| `/contact/` | Contact form |
| `/resume/` | Generated CV |
| `/register/` | Registration |
| `/login/` | Login |
| `/dashboard/` | Staff dashboard |
| `/admin/` | Django Admin |

## Project structure

```text
Name_ID_Portfolio/
├── manage.py
├── requirements.txt
├── Name_ID_Portfolio/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── Portfolio/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── management/commands/seed_portfolio.py
├── templates/Portfolio/
└── static/
    ├── css/style.css
    └── js/main.js
```

## Before submitting

- Rename the outer folder to your required `Name_ID_Portfolio` format.
- Replace the sample profile and project content with your own.
- Add real education, experience and skills.
- Run migrations and test registration, login, contact submission, resume and admin CRUD.
