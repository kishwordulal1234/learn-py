import random

print(" welcome in hangman ")

word_list = ["apple", "banana", "cattlehouse", "nepal", "kathmandu", "heaven", "lama", "lambda"]

chosen_words = random.choice(word_list)
#print(chosen_words)  # This line can be commented out once you don't need to see the word
print(" you get 10 guesses")

# Create the display_word list with underscores
display_word = []

# Initialize display_word with underscores for each letter in the chosen word
for letter in chosen_words:
    display_word += "_"

# Print the initial display_word
print(display_word)

# Initialize the number of incorrect guesses
num = 0

# Game over flag
game_over = False

# Main game loop
while not game_over:
    # Prompt the user to guess a letter
    guess = input("enter the guess letter: ").lower()

    # Check each position in the chosen_words
    for position in range(len(chosen_words)):
        letter = chosen_words[position]
        # If the guessed letter matches a letter in chosen_words, update display_word
        if letter == guess:
            display_word[position] = letter

    # If the guessed letter is not in chosen_words, increment the wrong guess counter
    if guess not in chosen_words:
        num += 1
        guess_left = 10 - num
        print(f"guess left: {guess_left}")
        # Check if the player has used all guesses
        if num >= 10:
            print(" you lose")
            print(f"The correct word was: {chosen_words}")  # Tell the user the correct word
            game_over = True

    # Print the current state of the display_word
    print(display_word)

    # Check if the player has guessed all the letters correctly
    if "_" not in display_word:
        print("you won")
        game_over = True
