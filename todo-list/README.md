# ✅ To-Do List App

A feature-rich desktop To-Do List application built with Python and CustomTkinter. Manage your tasks with priorities, categories, deadlines, and status tracking — all in a clean dark-mode GUI.

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Default Login](#default-login)
- [Screenshots](#screenshots)
- [Author](#author)

---

## About

This is a desktop task management application where users can register, log in, and manage their personal to-do lists. Tasks can be assigned a priority level, category, and deadline. The app tracks task status and highlights overdue items — all stored locally using CSV files.

---

## ✨ Features

### 🔐 Authentication
- User **Login** and **Registration** system
- Credentials stored securely in a local CSV file
- Default admin account included

### 📝 Task Management
- **Add tasks** with name, priority, category, and deadline
- **Update task status** — cycle through Pending → In Progress → Completed
- **Delete tasks** instantly
- Tasks sorted automatically by priority (High → Medium → Low)

### 📊 Dashboard
- Live **summary bar** showing count of Pending, In Progress, Completed, and Overdue tasks
- **Overdue detection** — tasks past their deadline are highlighted in red
- **Filter by status** — All / Pending / In Progress / Completed
- **Filter by category** — All / Work / Personal / Study / Shopping

### 🎨 UI & Design
- Modern **dark mode** GUI using CustomTkinter
- Color-coded **priority badges** (🔴 High / 🟡 Medium / 🟢 Low)
- Color-coded **status badges**
- Overdue tasks highlighted with red border
- Scrollable task list with card-style layout

---

## Requirements

- Python 3.8 or higher
- `customtkinter` library

Install the required library:

```bash
pip install customtkinter
```

---

## Installation

**1. Clone the repository:**

```bash
git clone https://github.com/your-username/todo-list-app.git
cd todo-list-app
```

**2. Install dependencies:**

```bash
pip install customtkinter
```

---

## ▶️ How to Run

```bash
python todo_app.py
```

On first run, the app automatically creates:
- `users.csv` — stores user credentials
- `tasks.csv` — stores all tasks

---

## 🕹️ How to Use

### Login / Register
1. Launch the app
2. Enter a **username** and **password**
3. Click **Login** to sign in or **Register** to create a new account

### Adding a Task
1. Click the **+ Add Task** button
2. Fill in:
   - Task name
   - Priority (High / Medium / Low)
   - Category (Work / Personal / Study / Shopping)
   - Deadline (format: `YYYY-MM-DD`)
3. Click **Add Task** to save

### Managing Tasks
| Action | How |
|--------|-----|
| Change status | Click **→ Next Status** button on the task card |
| Delete a task | Click the **Delete** button on the task card |
| Filter tasks | Use the sidebar radio buttons for Status or Category |

### Status Flow
```
Pending  →  In Progress  →  Completed  →  Pending (cycles)
```

---

## 📁 Project Structure

```
todo-list-app/
│
├── todo_app.py       # Main application script
├── users.csv         # Auto-generated: stores user accounts
├── tasks.csv         # Auto-generated: stores all tasks
└── README.md         # Project documentation
```

---

## 🔑 Default Login

A default admin account is created automatically on first launch:

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin123` |

> ⚠️ It is recommended to create your own account after first login.

---

## 🎨 Color Reference

### Priority Colors
| Priority | Color |
|----------|-------|
| 🔴 High | `#E24B4A` Red |
| 🟡 Medium | `#EF9F27` Orange |
| 🟢 Low | `#1D9E75` Green |

### Status Colors
| Status | Color |
|--------|-------|
| 🔵 Pending | `#378ADD` Blue |
| 🟡 In Progress | `#EF9F27` Orange |
| 🟢 Completed | `#1D9E75` Green |

---
