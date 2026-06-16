# ✅ To-Do List App

A modern, desktop-based To-Do List application built with Python and CustomTkinter. It features a clean dark UI with multi-user login, task management, priority tracking, and real-time status filtering — all stored locally using CSV files.

---

## Features

- Secure multi-user login and registration system
- Add tasks with priority, category, deadline, and status
- Filter tasks by status (Pending / In Progress / Completed) and category
- Tasks auto-sorted by priority — High → Medium → Low
- Live summary bar showing task counts and overdue alerts
- One-click status cycling and task deletion
- Overdue detection with visual highlights
- Fully persistent storage using local CSV files

---

## Requirements

- Python 3.8 or higher
- `customtkinter` library

Install the dependency with:

```bash
pip install customtkinter
```

---

## Usage

Run the application:

```bash
python todo_app.py
```

A login window will open. Use the default admin credentials to get started or register a new account.

**Default credentials:**
| Username | Password  |
|----------|-----------|
| `admin`  | `admin123`|

---

## How It Works

1. On first run, two CSV files are created — `users.csv` for accounts and `tasks.csv` for tasks.
2. After logging in, you land on the dashboard where all your tasks are displayed as cards.
3. Click **+ Add Task** to open the task form and fill in the name, priority, category, and deadline.
4. Use the sidebar to filter tasks by status or category instantly.
5. Each task card shows priority and status badges, deadline, and overdue warnings where applicable.
6. Use the arrow button to cycle a task's status forward, or the delete button to remove it.

---

## Task Properties

| Field      | Options                                      |
|------------|----------------------------------------------|
| Priority   | High, Medium, Low                            |
| Category   | Work, Personal, Study, Shopping              |
| Status     | Pending → In Progress → Completed            |
| Deadline   | Date in `YYYY-MM-DD` format                  |

---

## Data Storage

All data is stored in two local CSV files in the same directory as the script:

| File         | Contents                          |
|--------------|-----------------------------------|
| `users.csv`  | Registered usernames and passwords|
| `tasks.csv`  | All tasks across all users        |

> **Note:** Passwords are stored in plain text. This app is intended for local personal use and is not designed for production or shared environments.

---

> Found it useful? Give it a ⭐ on GitHub
