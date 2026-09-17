# 🌸 Hangman Game

A simple and interactive **Hangman Game** built using **Python and Streamlit**.

The player has to guess the name of a flower letter by letter. The game allows a maximum of **6 incorrect guesses**.

## 🎮 Live Demo

👉 **[Play the Hangman Game](https://projecthangmangame-sylofqdtmqvckr6orbkk7m.streamlit.app/)**

## ✨ Features

- 🌸 Flower-themed word guessing game
- 🎯 Random word selection
- 🔤 Letter-by-letter guessing
- ❌ Maximum of 6 incorrect guesses
- 🚫 Prevents repeated letter guesses
- 🏆 Displays a winning message when the word is guessed
- 😢 Displays the correct word when all tries are used
- 🔄 New Game option
- 🌐 Interactive Streamlit web interface

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Random module**

## 🧠 How It Works

1. The game randomly selects a flower name from a predefined list.
2. The selected word is initially displayed using underscores.
3. The player enters one letter at a time.
4. If the letter is present in the word, it is revealed.
5. If the letter is incorrect, one try is lost.
6. The player has a maximum of **6 incorrect guesses**.
7. The game ends when the complete word is guessed or all 6 incorrect guesses are used.

## 🌸 Available Words

The game currently uses the following flower names:

- Rose
- Lily
- Tulip
- Daisy
- Orchid

## 📂 Project Structure

```text
Hangman-Game/
│
├── hangman game.py
├── output with code.jpeg
└── README.md
