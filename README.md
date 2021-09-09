# Flask-Starter

Flask-Starter is a boilerplate starter template designed to help you quickstart your Flask web application development. It has all the ready-to-use bare minimum essentials.

## Features

- Flask 2.0, Python (`PEP8`)
- Signup, Login with (email, password)
- Forget/reset passwords
- Email verification
- User profile/password updates
- User roles (admin, user, staff)
- User profile status (active, inactive)
- Admin dashboard for management
- Contact us form
- Basic tasks/todo model (easily replace with your use-case)
- Bootstrap template (minimal)
- Utility scripts (initiate dummy database, run test server)
- Test & Production Configs
- Tests [To Do]


## Flask 2.0 `async` or not `async`

 - asynchronous support in Flask 2.0 is an amazing feature
 - however, use it only when it has a clear advantage over the equivalent synchronous code
 - write asynchronous code, if your application's routes, etc. are making heavy I/O-bound operations, like:
    - sending emails, making API calls to external servers, working with the file system, etc
 - otherwise, if your application is doing CPU-bound operations or long-running tasks, like:
    - processing images or large files, creating backups or running AI/ML models, etc
    - it is advised to use tools like "Celery" or "Huey", etc.


## `async` demo in our application

Check `emails/__init__.py` to see how emails being sent in `async` mode


## Primary Goals

 - To help you save lots of hours as a developer, even if for a hobby project or commercial project :-)
 - To provide basic features of standard web apps, while staying as unopinionated as possible 
 - To make back-end development quick to start, with robust foundations
 - To help you quickly learn how to build a Flask based web application
 - To help you quick start coding your web app's main logic and features


## Table of Contents

1. [Getting Started](#getting-started)
1. [Screenshots](#screenshots)
1. [Project Structure](#project-structure)
1. [Modules](#modules)
1. [Testing](#testing)
1. [Need Help?](#need-help)


## Getting Started

clone the project

```bash
$ git clone https://github.com/ksh7/flask-starter.git
$ cd flask-starter
```

create virtual environment using python3 and activate it (keep it outside our project directory)

```bash
$ python3 -m venv /path/to/your/virtual/environment
$ source <path/to/venv>/bin/activate
```

install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

setup `flask` command for our app

```bash
$ export FLASK_APP=manage.py
$ export FLASK_ENV=development
```

create instance folder in `/tmp` directory (sqlite database, temp files stay here)

```bash
$ mkdir /tmp/flaskstarter-instance
```

initialize database and get two default users (admin & demo), check `manage.py` for details

```bash
$ flask initdb
```

5) start test server at `localhost:5000`

```bash
$ flask run
```

## Screenshots

![Homepage](/screenshots/homepage.png)
![SignUp](/screenshots/signup.png)
![Login](/screenshots/login.png)
![Dashboard](/screenshots/dashboard.png)
![Tasks](/screenshots/tasks.png)
![Profile](/screenshots/profile.png)
![Admin](/screenshots/admin.png)


## Project Structure

```bash
flask-starter/
├── flaskstarter
│   ├── app.py
│   ├── config.py
│   ├── decorators.py
│   ├── emails
│   │   └── __init__.py
│   ├── extensions.py
│   ├── frontend
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── views.py
│   ├── __init__.py
│   ├── settings
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── views.py
│   ├── static
│   │   ├── bootstrap.bundle.min.js
│   │   ├── bootstrap.min.css
│   │   └── jquery.slim.min.js
│   ├── tasks
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── views.py
│   ├── templates
│   │   ├── admin
│   │   │   └── index.html
│   │   ├── dashboard
│   │   │   └── dashboard.html
│   │   ├── frontend
│   │   │   ├── change_password.html
│   │   │   ├── contact_us.html
│   │   │   ├── landing.html
│   │   │   ├── login.html
│   │   │   ├── reset_password.html
│   │   │   └── signup.html
│   │   ├── layouts
│   │   │   ├── base.html
│   │   │   └── header.html
│   │   ├── macros
│   │   │   ├── _confirm_account.html
│   │   │   ├── _flash_msg.html
│   │   │   ├── _form.html
│   │   │   └── _reset_password.html
│   │   ├── settings
│   │   │   ├── password.html
│   │   │   └── profile.html
│   │   └── tasks
│   │       ├── add_task.html
│   │       ├── edit_task.html
│   │       ├── my_tasks.html
│   │       └── view_task.html
│   ├── user
│   │   ├── constants.py
│   │   ├── __init__.py
│   │   └── models.py
│   └── utils.py
├── manage.py
├── README.md
├── requirements.txt
├── screenshots
└── tests
    ├── __init__.py
    └── test_flaskstarter.py
```


## Modules

This application uses the following modules

 - Flask
 - Flask-SQLAlchemy
 - Flask-WTF
 - Flask-Mail
 - Flask-Caching
 - Flask-Login
 - Flask-Admin
 - pytest
 - Bootstrap (bare minimum so that you can replace it with any frontend library)
 - Jinja2


## Testing

Note: This web application has been tested thoroughly during multiple large projects, however tests for this bare minimum version would be added in `tests` folder very soon to help you get started.

## Need Help? 🤝

If you need further help, reach out to me via [Twitter](https://twitter.com/kundan7_) DM.
