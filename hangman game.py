import streamlit as st
import random

# Choose a random flower
def choose_word():
    flowers = ["rose", "lily", "tulip", "daisy", "orchid"]
    return random.choice(flowers)

# Display hidden/revealed letters
def display_word(word, guessed_letters):
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display.strip()


# Page settings
st.set_page_config(
    page_title="Hangman Game",
    page_icon="🌸"
)

st.title("🌸 Hangman Game")
st.write("Guess the name of the flower!")
st.write("💡 Hint: The word is a flower.")
st.write("You have 6 incorrect guesses.")

# Start / reset game
if "word" not in st.session_state:
    st.session_state.word = choose_word()
    st.session_state.guessed_letters = []
    st.session_state.incorrect_guesses = 0
    st.session_state.game_over = False

# Display word
word = st.session_state.word
guessed_letters = st.session_state.guessed_letters

st.subheader(
    display_word(word, guessed_letters)
)

# Game input
if not st.session_state.game_over:

    guess = st.text_input(
        "Guess a letter:",
        max_chars=1
    ).lower()

    if st.button("Guess"):

        if not guess.isalpha():
            st.warning("Please enter a letter.")

        elif guess in guessed_letters:
            st.warning("You already guessed that letter!")

        else:
            guessed_letters.append(guess)

            if guess in word:
                st.success("Correct! 🎉")
            else:
                st.session_state.incorrect_guesses += 1
                st.error("Incorrect! ❌")

            # Check win
            if set(word).issubset(set(guessed_letters)):
                st.success(
                    f"🎉 Congratulations! You guessed the word: **{word}**"
                )
                st.session_state.game_over = True

            # Check loss
            elif st.session_state.incorrect_guesses >= 6:
                st.error(
                    f"😢 You ran out of guesses! The word was **{word}**"
                )
                st.session_state.game_over = True

# Game information
st.write(
    f"❌ Incorrect guesses: "
    f"{st.session_state.incorrect_guesses}/6"
)

st.write(
    f"❤️ Tries left: "
    f"{6 - st.session_state.incorrect_guesses}"
)

# Restart button
if st.button("🔄 New Game"):
    st.session_state.word = choose_word()
    st.session_state.guessed_letters = []
    st.session_state.incorrect_guesses = 0
    st.session_state.game_over = False
    st.rerun()
