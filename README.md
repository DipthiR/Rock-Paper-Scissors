# Rock-Paper-Scissors
# ✊✋✌️ Rock-Paper-Scissors Game

A simple and fun command-line **Rock-Paper-Scissors** game written in Python where you can play against the computer.

---

## 🎯 Features

- Command-line interface (CLI)
- Continuous play until the user chooses to exit
- Random computer move generation
- Win/Loss/Tie detection logic
- User input validation

---

## 📦 Requirements

- Python 3.x

No additional packages are required — just run the script with Python!

---

## 🚀 How to Run

### 1. Download or Clone the Script

```bash
git clone https://github.com/your-username/rock-paper-scissors.git
cd rock-paper-scissors
```
### 2. Run the Game

python rock_paper_scissors.py
If you're using Python 3 specifically, you might need to run python3 instead of python.

## 🎮 Gameplay Instructions
When you run the program, you’ll see a prompt like:

Choose:
1 - Rock
2 - Paper
3 - Scissors
0 - Exit
Type 1 for Rock, 2 for Paper, or 3 for Scissors.

Type 0 to exit the game.

The computer will randomly make its choice.

The result will display whether you win, lose, or tie.

## 💻 Example

Choose:
1 - Rock
2 - Paper
3 - Scissors
0 - Exit
Enter your choice (0/1/2/3): 2

You chose: Paper
Computer chose: Rock
You win!
## 🔧 Code Overview
python
Copy
Edit
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"
