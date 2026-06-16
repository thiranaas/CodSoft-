# 🎮 Rock · Paper · Scissors

A fun, interactive command-line Rock Paper Scissors game written in Python. Play against the computer, track your score across multiple rounds, and see who comes out on top — all from your terminal.

---

## Features

- Play against a randomized computer opponent
- Flexible input — accepts numbers (`1/2/3`), letters (`R/P/S`), or full words
- Live scoreboard updated after every round
- Final game summary with an overall winner verdict
- Graceful exit anytime with `Q` or `Ctrl+C`

---

## Usage

Run the script directly:

```bash
python rock_paper_scissors.py
```

You will be greeted with the game menu:

```
==================================================
       🎮  ROCK · PAPER · SCISSORS  🎮
==================================================

  Rules: Rock beats Scissors · Scissors beat Paper · Paper beats Rock
  Type 1/2/3 or R/P/S to play, Q to quit at any time.

  Choose your weapon:
    [1] 🪨  Rock
    [2] 📄  Paper
    [3] ✂️   Scissors
    [Q] 🚪  Quit

  Your choice:
```

---

## Input Options

| Input                 | Action      |
|-----------------------|-------------|
| `1`, `r`, `rock`      | 🪨 Rock     |
| `2`, `p`, `paper`     | 📄 Paper    |
| `3`, `s`, `scissors`  | ✂️ Scissors |
| `q`, `quit`, `exit`   | 🚪 Quit     |

---

## How It Works

1. The player selects Rock, Paper, or Scissors each round.
2. The computer makes a random choice independently.
3. The winner is determined using the classic rules — Rock beats Scissors, Scissors beat Paper, Paper beats Rock.
4. Scores are tracked across all rounds and displayed after each result.
5. At the end of the session, a full summary is shown with the overall winner.

---

## End of Game Summary

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
  Thanks for playing! 👋
==================================================
```

---

> If this made your coffee break a little more fun, give it a ⭐ on GitHub
