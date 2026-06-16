# 🐍 Python Projects Collection

A collection of three beginner-to-intermediate Python projects — a password generator, a terminal game, and a desktop task manager. Each project is self-contained, practical, and built with clean, readable code.

---

## 📁 Projects

| # | Project | Type | Description |
|---|---------|------|-------------|
| 1 | 🔐 Password Generator | CLI | Generate strong, customizable passwords instantly |
| 2 | 🎮 Rock · Paper · Scissors | CLI | Play against the computer with live score tracking |
| 3 | ✅ To-Do List App | Desktop GUI | Manage tasks with priorities, deadlines, and filters |

---

## 🔐 Password Generator

A lightweight, interactive command-line password generator. Create strong, randomized passwords with full control over length and character complexity — no external dependencies required.

### Features
- Customizable password length (minimum 4 characters)
- Optional inclusion of uppercase letters, digits, and symbols
- Guarantees at least one character from each selected category
- Shuffles the final password to eliminate predictable patterns
- Built-in password strength indicator (Weak / Moderate / Strong)
- Option to regenerate multiple passwords with the same settings

### Usage
```bash
python password_generator.py
```

```
=============================================
       🔐  PASSWORD GENERATOR  🔐
=============================================
Enter desired password length (minimum 4): 16

Customize complexity (press Enter to accept defaults):
  Include uppercase letters? (Y/n): y
  Include digits (0–9)?          (Y/n): y
  Include symbols (!@#...)?      (Y/n): y

=============================================
  Generated Password:  kR7#mQ2@zL9!pW4$
=============================================
  Password Length  :  16 characters
  Password Strength:  Strong 💪
=============================================
```

### Password Strength Criteria

| Strength    | Conditions                                                                |
|-------------|---------------------------------------------------------------------------|
| 💪 Strong   | Length ≥ 12 **and** uppercase + digits + symbols all enabled             |
| ⚠️ Moderate | Length ≥ 8 **and** at least one of uppercase, digits, or symbols enabled |
| Weak        | Any configuration that does not meet the above criteria                   |

### Security Note
This script uses Python's built-in `random` module, suitable for general-purpose use. For cryptographically secure passwords in production contexts, consider using `secrets.choice()` instead of `random.choice()`.

---

## 🎮 Rock · Paper · Scissors

A fun, interactive terminal game. Play against the computer, track your score across multiple rounds, and see who comes out on top.

### Features
- Play against a randomized computer opponent
- Flexible input — accepts numbers (`1/2/3`), letters (`R/P/S`), or full words
- Live scoreboard updated after every round
- Final game summary with an overall winner verdict
- Graceful exit anytime with `Q` or `Ctrl+C`

### Usage
```bash
python rock_paper_scissors.py
```

### Input Options

| Input                | Action      |
|----------------------|-------------|
| `1`, `r`, `rock`     | 🪨 Rock     |
| `2`, `p`, `paper`    | 📄 Paper    |
| `3`, `s`, `scissors` | ✂️ Scissors |
| `q`, `quit`, `exit`  | 🚪 Quit     |

### End of Game Summary
```
==================================================
           🏁  GAME OVER  🏁
==================================================
  Rounds played  :  5
  Your wins      :  3
  Computer wins  :  1
  Ties           :  1

  🏆  Overall Winner: YOU! Well played!
==================================================
```

---

## ✅ To-Do List App

A modern desktop task manager built with Python and CustomTkinter. Features a clean dark UI with multi-user login, task management, priority tracking, and real-time filtering — all stored locally using CSV files.

### Features
- Secure multi-user login and registration system
- Add tasks with priority, category, deadline, and status
- Filter tasks by status (Pending / In Progress / Completed) and category
- Tasks auto-sorted by priority — High → Medium → Low
- Live summary bar showing task counts and overdue alerts
- One-click status cycling and task deletion
- Overdue detection with visual highlights
- Fully persistent storage using local CSV files

### Requirements

```bash
pip install customtkinter
```

### Usage
```bash
python todo_app.py
```

**Default credentials:**

| Username | Password  |
|----------|-----------|
| `admin`  | `admin123`|

### Task Properties

| Field    | Options                               |
|----------|---------------------------------------|
| Priority | High, Medium, Low                     |
| Category | Work, Personal, Study, Shopping       |
| Status   | Pending → In Progress → Completed     |
| Deadline | Date in `YYYY-MM-DD` format           |

### Data Storage

| File        | Contents                           |
|-------------|------------------------------------|
| `users.csv` | Registered usernames and passwords |
| `tasks.csv` | All tasks across all users         |

> **Note:** Passwords are stored in plain text. This app is intended for local personal use and is not designed for production or shared environments.

---

## ⚙️ Requirements Overview

| Project               | Dependencies               | Python  |
|-----------------------|----------------------------|---------|
| Password Generator    | None (standard library)    | 3.6+    |
| Rock · Paper · Scissors | None (standard library)  | 3.6+    |
| To-Do List App        | `customtkinter`            | 3.8+    |

---

> If any of these projects were helpful, consider giving this repo a ⭐ on GitHub
