# 🔐 Password Generator

A simple and powerful command-line Password Generator built with Python. Generate strong, random passwords with full control over length and complexity — including uppercase letters, digits, and special symbols.

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [How to Use](#how-to-use)
- [Password Strength Guide](#password-strength-guide)
- [Project Structure](#project-structure)
- [Sample Output](#sample-output)
- [Author](#author)

---

## About

This project is a terminal-based Password Generator that allows users to create secure, randomized passwords based on their preferences. Users can specify the desired password length and choose which character types to include. The tool also evaluates and displays the strength of the generated password.

---

## ✨ Features

- 📏 Custom password length (minimum 4 characters)
- 🔠 Toggle uppercase letters (A–Z)
- 🔢 Toggle digits (0–9)
- 🔣 Toggle special symbols (!@#$%^&*...)
- ✅ Guarantees at least one character from each selected type
- 💪 Password strength indicator (Weak / Moderate / Strong)
- 🔁 Generate multiple passwords with the same settings
- ⚠️ Input validation — handles invalid entries gracefully

---

## Requirements

- Python 3.x (no external libraries needed)
- Only uses built-in modules: `random`, `string`

---

## ▶️ How to Run

**1. Clone or download the file:**

```bash
git clone https://github.com/your-username/password-generator.git
cd password-generator
```

**2. Run the script:**

```bash
python password_generator.py
```

---

## 🕹️ How to Use

1. Enter your desired **password length** (must be 4 or more)
2. Answer **Y/N** for each complexity option:
   - Include uppercase letters?
   - Include digits?
   - Include symbols?
3. Your **generated password** is displayed instantly
4. View the **strength indicator**
5. Choose to **generate another** with the same settings or exit

---

## 🛡️ Password Strength Guide

| Strength | Criteria |
|----------|----------|
| 💪 **Strong** | Length ≥ 12 AND uppercase + digits + symbols all enabled |
| ⚠️ **Moderate** | Length ≥ 8 AND at least one of uppercase / digits / symbols |
| ❌ **Weak** | Short length or minimal complexity options selected |

> 💡 **Tip:** For maximum security, use a length of **16 or more** with all complexity options enabled.

---

## 📁 Project Structure

```
password-generator/
│
├── password_generator.py    # Main generator script
└── README.md                # Project documentation
```

---

## 🖥️ Sample Output

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
  Generated Password:  r$T7@mKz!2Lp#Wq9
=============================================
  Password Length  :  16 characters
  Password Strength:  Strong 💪
=============================================

Generate another password with the same settings? (y/n): y

=============================================
  Generated Password:  X!9v@Qn3#mRt&Lk7
=============================================
  Password Length  :  16 characters
  Password Strength:  Strong 💪
=============================================

Generate another password with the same settings? (y/n): n

✅ Goodbye! Keep your passwords safe.
```

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
