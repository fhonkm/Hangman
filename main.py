from hangman_art import logo, stages
from hangman_list import words
import random

# extract from imports
hangman_logo = logo
chosen_word = random.choice(words)

# starting conds
print(logo)
end_of_game = False
display = []
guesses = []
lives = 6

# fill blanks
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

# logic
while not end_of_game:
    guess = input("guess a letter: ").lower()

    if guess in guesses:
        print("try another letter")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            guesses.append(guess)

    if guess not in chosen_word:
        print(f"'{guess}' is not in the word")
        lives -= 1
        print(f"lives left: {lives}")
        if lives == 0:
            end_of_game = True
            print("loser")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("winner winner chicken dinner!")

    print(stages[lives])