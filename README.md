# 🎮 Hangman Game (Python)

A simple command-line Hangman game written in Python. The game randomly selects a fruit name, and the player must guess the letters within 6 lives. Each wrong attempt progresses the hangman stage until the player wins or loses.

## 📌 Features
- Random fruit selection
- 6 lives with ASCII hangman stages
- Input validation (only one alphabet letter)
- Shows correct and incorrect guesses
- Win and lose messages

## 📂 Project Structure
hangman.py  
README.md

## ▶️ How to Run
1. Install Python 3.
2. Save the game as hangman.py.
3. Open terminal and run:
   python hangman.py

## 📝 Game Rules
- Guess one letter at a time.
- Only alphabet characters are allowed.
- You have 6 lives.
- Wrong guess → Hangman progresses.
- Correct guess → Letter revealed.
- All letters guessed → You win.
- Lives reach zero → Game over.

## 📊 Example Output
!!!!!!!!!!!HANGMAN GAME!!!!!!!!!!!
guess the fruit name  
total lives 6  
['_', '_', '_', '_', '_', '_']  
enter your guess: a  
correct guess  
['_', 'a', '_', '_', '_', '_']

## 🛠️ Technologies Used
- Python 3
- random module

## 🚀 Future Improvements
- Add more word categories
- Show already guessed letters
- Add scoring system
- Colorful output

## 📄 License
Free to use and modify.
