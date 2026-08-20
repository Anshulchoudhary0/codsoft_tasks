# solve 80 problems as well for AI and ML 
https://docs.google.com/document/d/1CuKacG3lnnt5B-7kB9p1DiJ2PLFW8TQWn9JG1lTYRJs/edit?tab=t.0#heading=h.ghy5ky51yxzv



# Python Mini Projects

A collection of three beginner-friendly, menu-driven Python command-line applications: a Password Generator, a Rock-Paper-Scissors Game, and a Contact Book.

---

## Table of Contents
- [Projects Overview](#projects-overview)
  - [1. Password Generator](#1-password-generator)
  - [2. Rock-Paper-Scissors Game](#2-rock-paper-scissors-game)
  - [3. Contact Book](#3-contact-book)
- [Prerequisites](#prerequisites)
- [How to Run in an IDE](#how-to-run-in-an-ide)
  - [Visual Studio Code](#option-1-visual-studio-code-vs-code)
  - [PyCharm](#option-2-pycharm)
  - [Terminal / Command Prompt](#option-3-terminal--command-prompt)

---

## Projects Overview

### 1. Password Generator (`task3_password_generator.py`)
Generates secure, customizable passwords.
- **Features:**
  - Custom password length specification.
  - Optional complexity toggles (uppercase letters, digits, special characters).
  - Built using Python's `random` and `string` modules.

### 2. Rock-Paper-Scissors Game (`rockpaper_scissors_game.py`)
An interactive, turn-based game against the computer.
- **Features:**
  - Dynamic user choice vs. randomized computer choice.
  - Automatic round winner determination.
  - Multi-round score tracking.
  - Option to replay or quit at any time.

### 3. Contact Book (`contact_book.py`)
A CRUD-based contact management application.
- **Features:**
  - **Add Contact:** Save name, phone number, email, and address.
  - **View Contacts:** List all stored contacts.
  - **Search Contact:** Search entries by name or phone number.
  - **Update Contact:** Modify existing contact information.
  - **Delete Contact:** Remove contacts with a confirmation check.

---

## Prerequisites

- **Python 3.x** installed from [python.org](https://www.python.org/downloads/) (ensure **"Add Python to PATH"** was checked during installation).
- No external packages needed (uses standard Python libraries).

---

## How to Run in an IDE

### Option 1: Visual Studio Code (VS Code)

1. **Open Project Folder:**
   - Launch VS Code.
   - Click `File` > `Open Folder...` and choose the folder containing your Python files.

2. **Verify Python Extension:**
   - Open the Extensions tab (`Ctrl+Shift+X` on Windows / `Cmd+Shift+X` on macOS).
   - Ensure the official **Python** extension (by Microsoft) is installed.

3. **Run the Script:**
   - Select any script (`task3_password_generator.py`, `rockpaper_scissors_game.py`, or `contact_book.py`) in the file explorer.
   - Click the **Run Python File (▷)** button in the top-right corner.
   - Interact with the program inside the integrated terminal at the bottom.

---

### Option 2: PyCharm

1. **Open Project:**
   - Launch PyCharm and click **Open**.
   - Select your project folder.

2. **Select Interpreter:**
   - Navigate to `File` > `Settings` > `Project: <folder_name>` > `Python Interpreter` (or `PyCharm` > `Settings` on macOS).
   - Ensure a Python 3.x interpreter is selected.

3. **Execute:**
   - Right-click the file you want to run from the left project panel.
   - Click **Run 'filename'**.
   - Use the interactive console window below to test.

---

### Option 3: Terminal / Command Prompt

You can also run any script directly from your terminal:

```bash
# Password Generator
python task3_password_generator.py

# Rock-Paper-Scissors Game
python rockpaper_scissors_game.py

# Contact Book
python contact_book.py
