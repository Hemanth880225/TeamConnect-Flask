# TeamConnect — Team Communication Platform

TeamConnect is a **Flask-based team communication platform** designed to enable users to share updates, collaborate, and interact in a structured environment. The application simulates a lightweight internal communication system similar to workplace collaboration tools.

This project demonstrates **full-stack Flask development**, **authentication systems**, and **modular backend architecture**.

---

# 🚀 Project Overview

TeamConnect allows users to:

* Register and login securely
* Create posts
* View team updates
* Edit and delete posts
* Manage user profile
* Upload profile pictures

The platform is designed with **clean architecture** and **scalable backend structure**.

---

# 🏗️ High-Level Architecture

```
┌──────────────────────────────────────────────┐
│                Client Layer                  │
│----------------------------------------------│
│ Browser | HTML | CSS | Bootstrap             │
└───────────────────────┬──────────────────────┘
                        │ HTTP Requests
                        ▼
┌──────────────────────────────────────────────┐
│               Flask Application              │
│----------------------------------------------│
│ Routes | Views | Templates                   │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│             Business Logic Layer             │
│----------------------------------------------│
│ Authentication | Post Management             │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│                Database Layer                │
│----------------------------------------------│
│ SQLAlchemy ORM | SQLite Database             │
└──────────────────────────────────────────────┘
```

---

# 📂 Project Structure

```
flaskblog
│
├── static
│   ├── main.css
│   └── profile_pics
│
├── templates
│   ├── layout.html
│   ├── home.html
│   ├── about.html
│   ├── login.html
│   ├── register.html
│   ├── account.html
│   ├── create_post.html
│   ├── post.html
│   └── user_post.html
│
├── __init__.py
├── forms.py
├── models.py
├── routes.py
└── README.md
```

---

# ⚙️ Tech Stack

## Backend

* Python
* Flask
* SQLAlchemy
* Flask-Login
* Flask-WTF

## Frontend

* HTML
* CSS
* Bootstrap
* Jinja2

## Database

* SQLite

---

# ✨ Features

## Authentication

* User Registration
* User Login
* Secure password hashing
* Session management

---

## Posts System

* Create posts
* Edit posts
* Delete posts
* View posts

---

## Profile Management

* Update profile
* Upload profile picture
* Update user details

---

# 🧠 Application Flow

```
User Registers / Login
        ↓
Access Dashboard
        ↓
Create Posts
        ↓
View Team Updates
        ↓
Interact with Content
```

---

# 🗄️ Database Design

## User Table

| Field      | Type    |
| ---------- | ------- |
| id         | Integer |
| username   | String  |
| email      | String  |
| image_file | String  |
| password   | String  |

---

## Post Table

| Field       | Type       |
| ----------- | ---------- |
| id          | Integer    |
| title       | String     |
| content     | Text       |
| date_posted | DateTime   |
| user_id     | ForeignKey |

---

# 🚀 Installation

Clone repository

```
git clone https://github.com/Hemanth880225/TeamConnect-Flask.git
```

Navigate

```
cd TeamConnect-Flask
```

Create virtual environment

```
python -m venv .venv
```

Activate

Windows

```
.venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run application

```
python run.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🧪 Learning Outcomes

This project demonstrates:

* Flask authentication
* Database relationships
* MVC architecture
* User session handling
* Profile management
* Full-stack Flask development

---

# 🔮 Future Improvements

* Comments system
* Notifications
* Real-time messaging
* Team channels
* File sharing

---

# ⭐ Resume Description

**TeamConnect — Team Communication Platform**
Built a team communication platform using Flask with authentication, post management, and profile system. Designed modular architecture using SQLAlchemy and implemented full-stack functionality with Bootstrap UI.

---

# 👨‍💻 Author

Hemanth
Backend Developer
Python | Flask | System Design

---

# License

MIT License
