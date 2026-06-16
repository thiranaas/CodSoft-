# 🔐 Password Generator

A lightweight, interactive command-line password generator written in Python. It lets you create strong, randomized passwords with full control over length and character complexity — no external dependencies required.

---

## Features

- Customizable password length (minimum 4 characters)
- Optional inclusion of uppercase letters, digits, and symbols
- Guarantees at least one character from each selected category
- Shuffles the final password to eliminate predictable patterns
- Built-in password strength indicator (Weak / Moderate / Strong)
- Option to regenerate multiple passwords with the same settings

---

## Usage

When you run the script, you will be guided through a short interactive prompt:

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

Generate another password with the same settings? (y/n): n

✅ Goodbye! Keep your passwords safe.
```

---

## Password Strength Criteria

| Strength     | Conditions                                                                 |
|--------------|----------------------------------------------------------------------------|
| 💪 Strong    | Length ≥ 12 **and** uppercase + digits + symbols all enabled              |
| ⚠️ Moderate  | Length ≥ 8 **and** at least one of uppercase, digits, or symbols enabled  |
| Weak         | Any configuration that does not meet the above criteria                    |

---

## How It Works

1. A character pool is built based on your selected options (lowercase is always included).
2. At least one character is picked from each enabled category to satisfy complexity requirements.
3. The remaining characters are filled randomly from the full pool.
4. The complete list is shuffled to remove any positional bias.
5. The final password is returned as a string.

---

## Security Note

This script uses Python's built-in `random` module, which is suitable for general-purpose password generation. For cryptographically secure passwords in production or security-sensitive contexts, consider using `secrets.choice()` instead of `random.choice()`.

---

> If this tool saved you time or made your workflow a little safer, consider giving it a ⭐ on GitHub
