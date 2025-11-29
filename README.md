# Hangman 🎯

A simple command-line Hangman game I created during my freshman year of High School in my introductory Python programming class. This project was one of my first experiences combining functions, file handling, loops, and ASCII-style animation.

## 🎮 Features

- Random word selection from a word list
- Text-based Hangman gameplay
- ASCII “loss” animations (progressively displayed)
- Tracks correct guesses, wrong guesses, and win/loss conditions
- Fully terminal-based — no external libraries required

## 📁 Project Structure

```bash
├── main.py         # Core game logic and input loop
├── animation.py    # ASCII animations shown on incorrect guesses / loss
└── Words.txt       # List of possible secret words
```

### Word List

The game randomly selects a secret word from Words.txt, which contains a large list of nouns used for gameplay.

## ▶️ How to Run

1. Clone the repoistory:

```bash
git clone https://github.com/MuhiburR/Hangman
cd Hangman
```

2. Run the game:

```bash
python3 main.py
```

Make sure your terminal supports ANSI text clearing if you want the animations and screen refreshes to work properly.

### 💡 Notes

- The game expects ALL CAPS input (as printed at program start).
- This project was created as a learning exercise, as seen by the amateur code.
- Could be subject to future improvements if considered.

### 📚 What I Learned

This was one of the first programs that taught me:

- How to work with files with Python
- Managing state inside a game loop
- Building functions to structure a program
- Handling user input
- Creating simple ASCII animations
