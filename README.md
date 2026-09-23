# 🌸 Hangman Game

A simple **flower-themed Hangman game** built with Python and Streamlit. Players guess a randomly selected flower name one letter at a time, with a maximum of 6 incorrect guesses.

## ✨ Features

* Random flower selection
* Letter-by-letter guessing
* Prevents repeated guesses
* Maximum of 6 incorrect guesses
* Win/loss detection
* New Game option
* Interactive Streamlit interface

## 🎮 How It Works

1. A flower is randomly selected from the predefined word list.
2. The word is displayed as hidden letters.
3. The player guesses one letter at a time.
4. Correct letters are revealed.
5. Incorrect guesses reduce the remaining attempts.
6. The game ends when the word is guessed or 6 incorrect guesses are reached.

### Available Words

`Rose · Lily · Tulip · Daisy · Orchid`

## 🛠️ Tech Stack

**Python · Streamlit · Random**

## 🌐 Live Demo

**Play:**
https://projecthangmangame-sylofqdtmqvckr6orbkk7m.streamlit.app/

## 🚀 Run Locally

Install Streamlit:

```bash
pip install streamlit
```

Run the game:

```bash
streamlit run "hangman game.py"
```

## 📁 Project Structure

```text
Hangman-Game/
├── hangman game.py
└── README.md
```

