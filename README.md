# 📝 Flask ToDo App

A simple ToDo application built with **Flask**, **PostgreSQL**, **SQLAlchemy**, **Flask-Login**, and **Docker**.

## 🚀 Features

- User Registration
- User Login & Logout
- Password Hashing
- User Authentication
- Create Tasks
- Complete / Undo Tasks
- Delete Tasks
- Task Deadlines
- Task Creation Date
- Flash Messages
- User-specific Task Management
- PostgreSQL Database
- Docker & Docker Compose Support

---

## 🛠 Technologies Used

- Python 3
- Flask
- Flask-Login
- Flask-SQLAlchemy
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- HTML
- Bootstrap 5

---

## 📂 Project Structure

```
ToDoApp/
│
├── app.py
├── config.py
├── models.py
├── extensions.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── templates/
│   ├── index.html
│   ├── login.html
│   └── register.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/atasamiloglu/ToDoApp.git
cd ToDoApp
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## 🐳 Run with Docker

Build and start the containers:

```bash
docker compose up --build
```

Stop the containers:

```bash
docker compose down
```

The application will be available at:

```
http://localhost:5000
```

---

## 📸 Screenshots

You can add screenshots of the application here.

Example:

- Login Page
- Register Page
- Dashboard
- Task Management

---

## 🔐 Authentication

- Secure password hashing
- User session management with Flask-Login
- Protected routes using `@login_required`

---

## 🗄 Database

PostgreSQL is used as the database.

Tables:

- Users
- Tasks

Each user can only view and manage their own tasks.

---

## 📄 License

This project was created for educational purposes.
