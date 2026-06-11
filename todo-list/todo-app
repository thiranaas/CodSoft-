import customtkinter as ctk
import csv
import os
from datetime import datetime, date
from tkinter import messagebox

# ─── File Paths ───────────────────────────────────────────────
USERS_FILE = "users.csv"
TASKS_FILE = "tasks.csv"

# ─── CSV Initialization ───────────────────────────────────────
def init_files():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password"])
            writer.writerow(["admin", "admin123"])

    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "task", "priority", "category", "deadline", "status"])


# ─── User Functions ───────────────────────────────────────────
def validate_user(username, password):
    with open(USERS_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                return True
    return False


def register_user(username, password):
    with open(USERS_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username:
                return False
    with open(USERS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, password])
    return True


# ─── Task Functions ───────────────────────────────────────────
def load_tasks(username):
    tasks = []
    with open(TASKS_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username:
                tasks.append(row)
    return tasks


def save_all_tasks(all_tasks):
    with open(TASKS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["username", "task", "priority", "category", "deadline", "status"])
        writer.writeheader()
        writer.writerows(all_tasks)


def load_all_tasks():
    tasks = []
    with open(TASKS_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append(row)
    return tasks


def add_task(username, task, priority, category, deadline):
    with open(TASKS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, task, priority, category, deadline, "Pending"])


def update_task_status(username, task_name, new_status):
    all_tasks = load_all_tasks()
    for t in all_tasks:
        if t["username"] == username and t["task"] == task_name:
            t["status"] = new_status
    save_all_tasks(all_tasks)


def delete_task_from_file(username, task_name):
    all_tasks = load_all_tasks()
    all_tasks = [t for t in all_tasks if not (t["username"] == username and t["task"] == task_name)]
    save_all_tasks(all_tasks)


# ─── Color Helpers ────────────────────────────────────────────
PRIORITY_COLORS = {
    "High":   "#E24B4A",
    "Medium": "#EF9F27",
    "Low":    "#1D9E75",
}

STATUS_COLORS = {
    "Pending":     "#378ADD",
    "In Progress": "#EF9F27",
    "Completed":   "#1D9E75",
}

def is_overdue(deadline_str):
    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        return deadline < date.today()
    except:
        return False


# ══════════════════════════════════════════════════════════════
#  LOGIN WINDOW
# ══════════════════════════════════════════════════════════════
def login_window():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("To-Do App — Login")
    root.geometry("420x520")
    root.resizable(False, False)

    # Header
    ctk.CTkLabel(root, text="✅ To-Do List", font=ctk.CTkFont(size=28, weight="bold")).pack(pady=(40, 4))
    ctk.CTkLabel(root, text="Stay organized. Stay focused.", font=ctk.CTkFont(size=13),
                 text_color="gray").pack(pady=(0, 30))

    frame = ctk.CTkFrame(root, corner_radius=16)
    frame.pack(padx=40, fill="x")

    ctk.CTkLabel(frame, text="Username", anchor="w", font=ctk.CTkFont(size=13)).pack(padx=20, pady=(20, 4), fill="x")
    username_entry = ctk.CTkEntry(frame, placeholder_text="Enter username", height=38)
    username_entry.pack(padx=20, fill="x")

    ctk.CTkLabel(frame, text="Password", anchor="w", font=ctk.CTkFont(size=13)).pack(padx=20, pady=(12, 4), fill="x")
    password_entry = ctk.CTkEntry(frame, placeholder_text="Enter password", show="*", height=38)
    password_entry.pack(padx=20, fill="x")

    msg_label = ctk.CTkLabel(frame, text="", text_color="#E24B4A", font=ctk.CTkFont(size=12))
    msg_label.pack(pady=(8, 0))

    def do_login():
        u = username_entry.get().strip()
        p = password_entry.get().strip()
        if not u or not p:
            msg_label.configure(text="Please fill in all fields.")
            return
        if validate_user(u, p):
            root.destroy()
            dashboard_window(u)
        else:
            msg_label.configure(text="Invalid username or password.")

    def do_register():
        u = username_entry.get().strip()
        p = password_entry.get().strip()
        if not u or not p:
            msg_label.configure(text="Please fill in all fields.")
            return
        if register_user(u, p):
            msg_label.configure(text="Account created! You can now log in.", text_color="#1D9E75")
        else:
            msg_label.configure(text="Username already exists.", text_color="#E24B4A")

    ctk.CTkButton(frame, text="Login", height=40, command=do_login,
                  font=ctk.CTkFont(size=14, weight="bold")).pack(padx=20, pady=(12, 8), fill="x")
    ctk.CTkButton(frame, text="Register", height=38, fg_color="transparent",
                  border_width=1, command=do_register,
                  font=ctk.CTkFont(size=13)).pack(padx=20, pady=(0, 20), fill="x")

    root.mainloop()


# ══════════════════════════════════════════════════════════════
#  DASHBOARD WINDOW
# ══════════════════════════════════════════════════════════════
def dashboard_window(username):
    root = ctk.CTk()
    root.title(f"To-Do — {username}")
    root.geometry("820x620")
    root.resizable(True, True)

    selected_filter = ctk.StringVar(value="All")
    selected_category_filter = ctk.StringVar(value="All")

    # ── Sidebar ───────────────────────────────────────────────
    sidebar = ctk.CTkFrame(root, width=200, corner_radius=0)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    ctk.CTkLabel(sidebar, text="✅ To-Do", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(30, 4))
    ctk.CTkLabel(sidebar, text=f"@{username}", font=ctk.CTkFont(size=12),
                 text_color="gray").pack(pady=(0, 30))

    ctk.CTkLabel(sidebar, text="STATUS FILTER", font=ctk.CTkFont(size=11),
                 text_color="gray").pack(padx=16, anchor="w")

    for status in ["All", "Pending", "In Progress", "Completed"]:
        ctk.CTkRadioButton(sidebar, text=status, variable=selected_filter,
                           value=status, command=lambda: refresh_tasks()).pack(
            padx=20, pady=4, anchor="w")

    ctk.CTkLabel(sidebar, text="CATEGORY", font=ctk.CTkFont(size=11),
                 text_color="gray").pack(padx=16, pady=(20, 4), anchor="w")

    for cat in ["All", "Work", "Personal", "Study", "Shopping"]:
        ctk.CTkRadioButton(sidebar, text=cat, variable=selected_category_filter,
                           value=cat, command=lambda: refresh_tasks()).pack(
            padx=20, pady=3, anchor="w")

    ctk.CTkButton(sidebar, text="Logout", fg_color="transparent", border_width=1,
                  command=lambda: [root.destroy(), login_window()]).pack(
        padx=16, pady=30, side="bottom", fill="x")

    # ── Main Area ─────────────────────────────────────────────
    main = ctk.CTkFrame(root, fg_color="transparent")
    main.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    # Summary bar
    summary_frame = ctk.CTkFrame(main, corner_radius=12)
    summary_frame.pack(fill="x", pady=(0, 16))

    pending_lbl   = ctk.CTkLabel(summary_frame, text="", font=ctk.CTkFont(size=13))
    inprog_lbl    = ctk.CTkLabel(summary_frame, text="", font=ctk.CTkFont(size=13))
    complete_lbl  = ctk.CTkLabel(summary_frame, text="", font=ctk.CTkFont(size=13))
    overdue_lbl   = ctk.CTkLabel(summary_frame, text="", font=ctk.CTkFont(size=13), text_color="#E24B4A")

    pending_lbl.pack(side="left", padx=16, pady=10)
    inprog_lbl.pack(side="left", padx=16, pady=10)
    complete_lbl.pack(side="left", padx=16, pady=10)
    overdue_lbl.pack(side="left", padx=16, pady=10)

    # Add task button
    ctk.CTkButton(main, text="+ Add Task", height=38,
                  font=ctk.CTkFont(size=13, weight="bold"),
                  command=lambda: add_task_dialog()).pack(anchor="e", pady=(0, 12))

    # Task list
    scroll = ctk.CTkScrollableFrame(main, corner_radius=12)
    scroll.pack(fill="both", expand=True)

    # ── Refresh / Render Tasks ────────────────────────────────
    def refresh_tasks():
        for widget in scroll.winfo_children():
            widget.destroy()

        tasks = load_tasks(username)

        # Update summary
        pending  = sum(1 for t in tasks if t["status"] == "Pending")
        inprog   = sum(1 for t in tasks if t["status"] == "In Progress")
        complete = sum(1 for t in tasks if t["status"] == "Completed")
        overdue  = sum(1 for t in tasks if is_overdue(t["deadline"]) and t["status"] != "Completed")

        pending_lbl.configure(text=f"🔵 Pending: {pending}")
        inprog_lbl.configure(text=f"🟡 In Progress: {inprog}")
        complete_lbl.configure(text=f"🟢 Completed: {complete}")
        overdue_lbl.configure(text=f"🔴 Overdue: {overdue}" if overdue > 0 else "")

        # Filter
        sf = selected_filter.get()
        cf = selected_category_filter.get()
        filtered = [t for t in tasks
                    if (sf == "All" or t["status"] == sf)
                    and (cf == "All" or t["category"] == cf)]

        # Sort: High → Medium → Low
        priority_order = {"High": 0, "Medium": 1, "Low": 2}
        filtered.sort(key=lambda t: priority_order.get(t["priority"], 3))

        if not filtered:
            ctk.CTkLabel(scroll, text="No tasks found.", text_color="gray",
                         font=ctk.CTkFont(size=14)).pack(pady=40)
            return

        for task in filtered:
            render_task_card(task)

    def render_task_card(task):
        overdue = is_overdue(task["deadline"]) and task["status"] != "Completed"

        card = ctk.CTkFrame(scroll, corner_radius=10, border_width=1,
                            border_color="#E24B4A" if overdue else "gray25")
        card.pack(fill="x", pady=5, padx=4)

        top = ctk.CTkFrame(card, fg_color="transparent")
        top.pack(fill="x", padx=14, pady=(12, 4))

        # Task name
        ctk.CTkLabel(top, text=task["task"], font=ctk.CTkFont(size=14, weight="bold"),
                     anchor="w").pack(side="left")

        # Priority badge
        p_color = PRIORITY_COLORS.get(task["priority"], "gray")
        ctk.CTkLabel(top, text=f"  {task['priority']}  ",
                     fg_color=p_color, corner_radius=6,
                     font=ctk.CTkFont(size=11), text_color="white").pack(side="right", padx=4)

        # Status badge
        s_color = STATUS_COLORS.get(task["status"], "gray")
        ctk.CTkLabel(top, text=f"  {task['status']}  ",
                     fg_color=s_color, corner_radius=6,
                     font=ctk.CTkFont(size=11), text_color="white").pack(side="right", padx=4)

        # Meta row
        meta = ctk.CTkFrame(card, fg_color="transparent")
        meta.pack(fill="x", padx=14, pady=(0, 10))

        deadline_text = f"📅 {task['deadline']}"
        if overdue:
            deadline_text += "  ⚠ Overdue"
        ctk.CTkLabel(meta, text=f"📁 {task['category']}   {deadline_text}",
                     font=ctk.CTkFont(size=12), text_color="gray").pack(side="left")

        # Action buttons
        btn_frame = ctk.CTkFrame(meta, fg_color="transparent")
        btn_frame.pack(side="right")

        statuses = ["Pending", "In Progress", "Completed"]
        current_idx = statuses.index(task["status"]) if task["status"] in statuses else 0
        next_status = statuses[(current_idx + 1) % len(statuses)]

        ctk.CTkButton(btn_frame, text=f"→ {next_status}", width=110, height=28,
                      font=ctk.CTkFont(size=11),
                      command=lambda t=task["task"], s=next_status: [
                          update_task_status(username, t, s), refresh_tasks()
                      ]).pack(side="left", padx=4)

        ctk.CTkButton(btn_frame, text="Delete", width=70, height=28,
                      fg_color="#993C1D", hover_color="#E24B4A",
                      font=ctk.CTkFont(size=11),
                      command=lambda t=task["task"]: [
                          delete_task_from_file(username, t), refresh_tasks()
                      ]).pack(side="left")

    # ── Add Task Dialog ───────────────────────────────────────
    def add_task_dialog():
        dialog = ctk.CTkToplevel(root)
        dialog.title("Add New Task")
        dialog.geometry("400x460")
        dialog.resizable(False, False)
        dialog.grab_set()

        ctk.CTkLabel(dialog, text="New Task", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(24, 16))

        form = ctk.CTkFrame(dialog, fg_color="transparent")
        form.pack(padx=24, fill="x")

        ctk.CTkLabel(form, text="Task Name", anchor="w").pack(fill="x", pady=(0, 4))
        task_entry = ctk.CTkEntry(form, placeholder_text="e.g. Complete assignment", height=36)
        task_entry.pack(fill="x")

        ctk.CTkLabel(form, text="Priority", anchor="w").pack(fill="x", pady=(12, 4))
        priority_var = ctk.StringVar(value="Medium")
        ctk.CTkOptionMenu(form, variable=priority_var,
                          values=["High", "Medium", "Low"]).pack(fill="x")

        ctk.CTkLabel(form, text="Category", anchor="w").pack(fill="x", pady=(12, 4))
        category_var = ctk.StringVar(value="Personal")
        ctk.CTkOptionMenu(form, variable=category_var,
                          values=["Work", "Personal", "Study", "Shopping"]).pack(fill="x")

        ctk.CTkLabel(form, text="Deadline (YYYY-MM-DD)", anchor="w").pack(fill="x", pady=(12, 4))
        deadline_entry = ctk.CTkEntry(form, placeholder_text=str(date.today()), height=36)
        deadline_entry.pack(fill="x")

        err_label = ctk.CTkLabel(form, text="", text_color="#E24B4A", font=ctk.CTkFont(size=12))
        err_label.pack(pady=(8, 0))

        def submit():
            t = task_entry.get().strip()
            d = deadline_entry.get().strip()
            if not t:
                err_label.configure(text="Task name cannot be empty.")
                return
            try:
                datetime.strptime(d, "%Y-%m-%d")
            except ValueError:
                err_label.configure(text="Invalid date format. Use YYYY-MM-DD.")
                return
            add_task(username, t, priority_var.get(), category_var.get(), d)
            dialog.destroy()
            refresh_tasks()

        ctk.CTkButton(dialog, text="Add Task", height=40,
                      font=ctk.CTkFont(size=13, weight="bold"),
                      command=submit).pack(padx=24, pady=20, fill="x")

    refresh_tasks()
    root.mainloop()

if __name__ == "__main__":
    init_files()
    login_window()
