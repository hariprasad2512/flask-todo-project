# Task Smash

Task Smash is a lightweight Flask-based task management application that helps users keep track of daily work by adding, viewing, editing, and deleting tasks. It is a simple CRUD project designed to demonstrate how to build a small database-driven web app with Python, Flask, and SQLite.

This project is ideal for beginners learning web development with Flask, or anyone who wants a minimal but functional to-do list app that can run locally on a laptop or desktop computer.

## What this project does

Task Smash allows users to:

- Add a new task
- View all saved tasks
- Update an existing task
- Delete completed or unnecessary tasks
- Store all task records in a local SQLite database

The app uses Flask for routing and rendering, SQLAlchemy for database interaction, and Jinja templates for the frontend UI.

## Technologies used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2
- HTML
- CSS
- Flask-Scss

## Project structure

- `app.py` — Main Flask application, database setup, and task routes
- `templates/` — HTML templates for the home page and edit page
- `static/styles.css` — Styling for the application
- `requirements.txt` — Python package dependencies
- `instance/` — Local instance folder used by Flask apps

## Features overview

- Clean, minimal task dashboard
- Quick task creation from the home page
- Edit task details from a dedicated form
- Delete tasks directly from the list
- Automatic database creation on first run

## Local installation

Follow the steps below to install and run the app on your local machine.

### 1. Prerequisites

Make sure you have Python 3.10 or newer installed on your machine.

To check your Python version:

```bash
python --version
```

If Python is not installed, install it from the official Python website and then reopen your terminal.

### 2. Clone or download the project

```bash
git clone https://github.com/hariprasad2512/flask-todo-project.git
cd flask-todo-project
```

If you are using the project from a downloaded zip file, extract it first and then move into the project folder.

### 3. Create a virtual environment

On macOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

After starting the app, Flask will usually run a local server at:

```text
http://127.0.0.1:5000/
```

Open that address in your browser to use the application.

## How the app works

When the app starts:

- A Flask web server is launched
- The SQLite database is created if it does not exist
- The task model is initialized
- The app loads the homepage where tasks are displayed

Users can then:

- Submit a task in the form at the top of the page
- Click edit to change a task
- Click delete to remove a task

## Database behavior

The application uses SQLAlchemy with SQLite and stores tasks in a database file named `tasks_database.db` that is generated automatically when the app is first run. This means no manual database setup is required for a simple local development setup.

## Development notes

This project is intentionally simple and beginner-friendly. It is a good example of:

- Flask route handling
- Database modeling with SQLAlchemy
- HTML form processing
- Template rendering with Jinja
- Local persistence using SQLite

## Common troubleshooting

### Module not found errors

If you see a missing dependency error, reinstall the requirements:

```bash
pip install -r requirements.txt
```

### Port already in use

If port 5000 is already being used by another application, stop that process or change the port in `app.py`.

### Database not creating

Make sure you run the app from the project root directory and that the Python environment is active.

## License

This project is intended for learning and local development use.

## Summary

Task Smash is a simple personal task tracker built with Flask and SQLite. It provides a practical example of a CRUD web application and is easy to run on a local machine for learning, prototyping, or personal use.
