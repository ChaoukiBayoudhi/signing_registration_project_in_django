# Signing registration project in Django

A Django project with 2 models and HTML templates.

## Tech stack

- Python 3
- Django
- Database: SQLite

## Project structure

- `signing_registration_project/`: project settings and root URLs
- `signing_registration_app/`: Django app
- 4 HTML templates
- Tests: `signing_registration_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `CustomUserManager` | `signing_registration_app` | — |
| `CustomUser` | `signing_registration_app` | email, first_name, last_name, photo, birthday, is_active, is_staff, date_joined |

## URL routes

Declared in `urls.py`:

- `/register/`
- `/login/`
- `/logout/`
- `/password_reset/`
- `/password_reset/done/`
- `/reset/<uidb64>/<token>/`
- `/reset/done/`
- `/blog/`
- `/accounts/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
```

There is no `requirements.txt`; the packages above are the ones the settings and imports refer to.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
