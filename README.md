## How to Run the Projects in an IDE

### Prerequisites
- Install **Python 3.x** from [python.org](https://www.python.org/downloads/) (make sure to check **"Add Python to PATH"** during installation).
- No external libraries are required (all scripts use Python's standard library).

---

### Option 1: Visual Studio Code (VS Code)

1. **Open the Project Folder:**
   - Launch VS Code.
   - Go to `File` > `Open Folder...` and select the folder containing the `.py` files.

2. **Install the Python Extension:**
   - Click the **Extensions** icon on the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`).
   - Search for **Python** (by Microsoft) and click **Install**.

3. **Select Python Interpreter:**
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac).
   - Type and select `Python: Select Interpreter`, then choose your installed Python 3 version.

4. **Run the Script:**
   - Open any file (e.g., `task3_password_generator.py`).
   - Click the **Play (▷)** button in the top-right corner, or right-click anywhere in the editor and choose **Run Python File in Terminal**.
   - Interact with the program inside the integrated terminal at the bottom.

---

### Option 2: PyCharm

1. **Open the Project:**
   - Launch PyCharm and select `Open`.
   - Browse to and open your project folder.

2. **Configure Python Interpreter:**
   - Go to `File` > `Settings` > `Project: <folder_name>` > `Python Interpreter` (on macOS: `PyCharm` > `Preferences`).
   - Ensure a valid Python 3 interpreter is selected.

3. **Run the Script:**
   - Right-click the file you want to execute (e.g., `task4_rock_paper_scissors.py`) in the Project tree on the left.
   - Select **Run 'task4_rock_paper_scissors'**.
   - The interactive console will open at the bottom.

---

### Option 3: Terminal / Command Prompt

You can also run any script directly via your terminal:

```bash
# Task 3: Password Generator
python task3_password_generator.py

# Task 4: Rock-Paper-Scissors Game
python task4_rock_paper_scissors.py

# Task 5: Contact Book
python task5_contact_book.py
