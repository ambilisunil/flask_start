# README.md


Explanation of Files

### **1️⃣ `server.py` (Simple Flask App)**
A single-file Flask application demonstrating basic routes and form handling.

### **2️⃣ `app.py` (Flask App with Blueprint Routing)**
- Uses **Blueprints** to modularize routes.
- Registers `home.py` and `user.py`.
- Runs on `http://127.0.0.1:5000/`

### **3️⃣ `todoapp.py` (MongoDB Integrated Todo App)**
- Uses **MongoDB** to store and manage tasks.
- Implements **CRUD operations** (Add, View, Delete tasks).
- Uses `todo.html` as the frontend template.

 Flask MongoDB Todo App

This repository contains a simple Flask-based Task Manager application with MongoDB integration.
The project demonstrates how to structure a Flask app with modular routes, use MongoDB as a database, and create basic CRUD functionalities.

---

## 🎯 API Routes
| Route               | Method  | Description |
|---------------------|---------|-------------|
| `/`                 | GET     | Home Page |
| `/user/<name>`      | GET     | Displays user profile |
| `/form`            | GET/POST | Handles form input |
| `/api/data`        | GET     | Returns sample API response |
| `/add`             | POST    | Adds a task to MongoDB |
| `/delete/<task_id>` | GET     | Deletes a task from MongoDB |

---

