import random
import sys

# ── Constants ────────────────────────────────────────────────────────────────
CHOICES   = ["rock", "paper", "scissors"]
EMOJI     = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
# What each choice beats
BEATS     = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# ── Display helpers ──────────────────────────────────────────────────────────
def clear_line():
    print()

def banner():
    print("=" * 50)
    print("       🎮  ROCK · PAPER · SCISSORS  🎮")
    print("=" * 50)

def scoreboard(scores, rounds):
    print(f"\n  📊  Scoreboard  (Round {rounds})")
    print(f"  {'You':>10}  :  {scores['player']:<5}"
          f"{'Computer':>10}  :  {scores['computer']:<5}"
          f"{'Ties':>6}  :  {scores['tie']}")
    print("-" * 50)

def show_result(player_choice, computer_choice, outcome):
    p = f"{EMOJI[player_choice]}  {player_choice.capitalize()}"
    c = f"{EMOJI[computer_choice]}  {computer_choice.capitalize()}"
    print(f"\n  You chose    →  {p}")
    print(f"  Computer chose →  {c}")
    print()
    if outcome == "win":
        print("  🎉  You WIN!  "
              f"{player_choice.capitalize()} beats {computer_choice}.")
    elif outcome == "lose":
        print("  💀  You LOSE!  "
              f"{computer_choice.capitalize()} beats {player_choice}.")
    else:
        print("  🤝  It's a TIE!")

# ── Core logic ───────────────────────────────────────────────────────────────
def computer_choice():
    return random.choice(CHOICES)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif BEATS[player] == computer:
        return "win"
    else:
        return "lose"

# ── Input helpers ────────────────────────────────────────────────────────────
def get_player_choice():
    """Prompt until the user enters a valid choice or quits."""
    print("\n  Choose your weapon:")
    print("    [1] 🪨  Rock")
    print("    [2] 📄  Paper")
    print("    [3] ✂️   Scissors")
    print("    [Q] 🚪  Quit")

    mapping = {
        "1": "rock",   "r": "rock",   "rock": "rock",
        "2": "paper",  "p": "paper",  "paper": "paper",
        "3": "scissors","s": "scissors","scissors": "scissors",
    }

    while True:
        raw = input("\n  Your choice: ").strip().lower()
        if raw in ("q", "quit", "exit"):
            return None
        if raw in mapping:
            return mapping[raw]
        print("  ⚠️  Invalid input. Enter 1/2/3, R/P/S, or Q to quit.")

def ask_play_again():
    while True:
        ans = input("\n  Play another round? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("  Please enter 'y' or 'n'.")

# ── Main game loop ───────────────────────────────────────────────────────────
def main():
    banner()
    print("\n  Rules: Rock beats Scissors · Scissors beat Paper · Paper beats Rock")
    print("  Type 1/2/3 or R/P/S to play, Q to quit at any time.\n")

    scores = {"player": 0, "computer": 0, "tie": 0}
    rounds = 0

    while True:
        player = get_player_choice()

        if player is None:          # user chose to quit
            break

        comp   = computer_choice()
        result = determine_winner(player, comp)
        rounds += 1

        # Update scores
        if result == "win":
            scores["player"] += 1
        elif result == "lose":
            scores["computer"] += 1
        else:
            scores["tie"] += 1

        print("\n" + "-" * 50)
        show_result(player, comp, result)
        scoreboard(scores, rounds)

        if not ask_play_again():
            break

    # ── Final summary ────────────────────────────────────────────────────────
    clear_line()
    print("=" * 50)
    print("           🏁  GAME OVER  🏁")
    print("=" * 50)
    if rounds == 0:
        print("  No rounds played. Come back and try next time!")
    else:
        print(f"  Rounds played  :  {rounds}")
        print(f"  Your wins      :  {scores['player']}")
        print(f"  Computer wins  :  {scores['computer']}")
        print(f"  Ties           :  {scores['tie']}")
        clear_line()
        # Overall verdict
        if scores["player"] > scores["computer"]:
            print("  🏆  Overall Winner: YOU! Well played!")
        elif scores["computer"] > scores["player"]:
            print("  🤖  Overall Winner: Computer. Better luck next time!")
        else:
            print("  🤝  Overall Result: Perfectly tied!")
    print("=" * 50)
    print("  Thanks for playing! 👋")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Game interrupted. Goodbye! 👋")
        sys.exit(0)
