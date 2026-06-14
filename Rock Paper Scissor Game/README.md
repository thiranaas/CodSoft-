# 🎮 Rock · Paper · Scissors

A simple yet feature-rich command-line Rock Paper Scissors game built with Python. Play against the computer, track your score across multiple rounds, and see a final summary at the end!

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Project Structure](#project-structure)
- [Sample Output](#sample-output)
- [Author](#author)

---

## About

This project is a terminal-based Rock Paper Scissors game where the user competes against the computer. The computer makes a random choice each round, and the winner is determined based on classic game rules. Scores are tracked across all rounds with a final summary displayed at the end.

---

## ✨ Features

- 🪨 📄 ✂️ Choose Rock, Paper, or Scissors using numbers or letters
- 🤖 Random computer selection each round
- 🏆 Winner determination with clear feedback
- 📊 Live scoreboard after every round
- 🔁 Play as many rounds as you want
- 🏁 Final game summary with overall winner
- ⚠️ Input validation — handles invalid entries gracefully
- 🚪 Quit anytime by pressing `Q` or `Ctrl+C`

---

## Requirements

- Python 3.x (no external libraries needed)
- Only uses built-in modules: `random`, `sys`

---

## ▶️ How to Run

**1. Clone or download the file:**

```bash
git clone https://github.com/your-username/rock-paper-scissors.git
cd rock-paper-scissors
```

**2. Run the script:**

```bash
python rock_paper_scissors.py
```

---

## 🕹️ How to Play

When prompted, enter your choice using any of these formats:

| Input | Meaning |
|-------|---------|
| `1` or `R` or `rock` | 🪨 Rock |
| `2` or `P` or `paper` | 📄 Paper |
| `3` or `S` or `scissors` | ✂️ Scissors |
| `Q` or `quit` | 🚪 Quit the game |

> Input is **case-insensitive** — `R`, `r`, and `ROCK` all work.

---

## 📏 Game Rules

- 🪨 **Rock** beats ✂️ Scissors
- ✂️ **Scissors** beats 📄 Paper
- 📄 **Paper** beats 🪨 Rock
- Same choice = 🤝 Tie

---

## 📁 Project Structure

```
rock-paper-scissors/
│
├── rock_paper_scissors.py   # Main game script
└── README.md                # Project documentation
```

---

## 🖥️ Sample Output

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

  Your choice: 1

--------------------------------------------------
  You chose      →  🪨  Rock
  Computer chose →  ✂️  Scissors

  🎉  You WIN!  Rock beats scissors.

  📊  Scoreboard  (Round 1)
        You  :  1       Computer  :  0    Ties  :  0
--------------------------------------------------

  Play another round? (y/n): n

==================================================
           🏁  GAME OVER  🏁
==================================================
  Rounds played  :  1
  Your wins      :  1
  Computer wins  :  0
  Ties           :  0

  🏆  Overall Winner: YOU! Well played!
==================================================
  Thanks for playing! 👋
==================================================
---
