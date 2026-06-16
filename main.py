import os
import sys
import subprocess

# ─── Display Helpers ──────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print("=" * 52)
    print("         🐍  PYTHON PROJECTS COLLECTION")
    print("=" * 52)
    print("  A collection of three standalone Python projects.")
    print("=" * 52)

def menu():
    print("\n  Select a project to launch:\n")
    print("    [1]  🔐  Password Generator")
    print("    [2]  🎮  Rock · Paper · Scissors")
    print("    [3]  ✅  To-Do List App")
    print()
    print("    [Q]  🚪  Quit")
    print()

# ─── Project Launchers ────────────────────────────────────────
def launch_password_generator():
    path = os.path.join("Password Generator", "password_generator.py")
    if not os.path.exists(path):
        print("\n  ⚠️  File not found: Password Generator/password_generator.py")
        return
    print("\n  Launching Password Generator...\n")
    print("=" * 52)
    subprocess.run([sys.executable, path])

def launch_rock_paper_scissors():
    path = os.path.join("Rock Paper Scissor Game", "rock_paper_scissor_game.py")
    if not os.path.exists(path):
        print("\n  ⚠️  File not found: Rock Paper Scissor Game/rock_paper_scissor_game.py")
        return
    print("\n  Launching Rock · Paper · Scissors...\n")
    print("=" * 52)
    subprocess.run([sys.executable, path])

def launch_todo_app():
    path = os.path.join("todo-list", "todo-app.py")
    if not os.path.exists(path):
        print("\n  ⚠️  File not found: todo-list/todo-app.py")
        return
    try:
        import customtkinter  # noqa: F401
    except ImportError:
        print("\n  ⚠️  Missing dependency: customtkinter")
        print("  Install it with:  pip install customtkinter\n")
        return
    print("\n  Launching To-Do List App...\n")
    print("=" * 52)
    subprocess.run([sys.executable, path])

# ─── Input Handler ────────────────────────────────────────────
def get_choice():
    return input("  Your choice: ").strip().lower()

# ─── Main Loop ────────────────────────────────────────────────
def main():
    clear()
    banner()

    handlers = {
        "1": launch_password_generator,
        "2": launch_rock_paper_scissors,
        "3": launch_todo_app,
    }

    while True:
        menu()
        choice = get_choice()

        if choice in ("q", "quit", "exit"):
            print("\n  👋  Goodbye! Happy coding.\n")
            print("=" * 52)
            break
        elif choice in handlers:
            clear()
            handlers[choice]()
            print("\n" + "=" * 52)
            input("\n  Press Enter to return to the main menu...")
            clear()
            banner()
        else:
            print("\n  ⚠️  Invalid choice. Please enter 1, 2, 3, or Q.")

if __name__ == "__main__":
    main()
