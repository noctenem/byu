import random

"""
Program: Word Puzzle
Author: Sairi Conejo Flores

Purpose: Creating a word puzzle game with loops
"""
# The game includes a feature where there are difficulty.
# The "random" library was imported to choose a word at random based
# on the chosen level.

def game():
    guesses = 0
    correct_guess = False

    levels = [
        ["car", "sun", "fun"],                    # easy
        ["monster", "soccer"],         # normal
        ["basketball", "calculator"]   # hard
    ]

    message = """
Welcome to the exciting Word Guessing Game!
Your goal is to guess the secret word by trying different words.
\nChoose the difficulty level:\n
Easy (Press 1)
Normal (Press 2)
Hard (Press 3)\n                               
"""

    difficulty_level = int(input(message))
    
    while difficulty_level < 1 or difficulty_level > 3:
        difficulty_level = int(input(message))

    # Choose a random word based on the difficulty level.
    word = random.choice(levels[difficulty_level - 1])
    
    # underscores
    hints = ["_ "] * len(word)
    print(f"Your hint is: {''.join(hints).strip()}")

    while not correct_guess:
        user_input = input("What is your guess?: ").lower().strip()

        guesses += 1
        if len(user_input) != len(word):
            print("""
Sorry, the guess must have the same number of letters as the secret word.
""")
            continue # This ensures that the attempt doesn't count in the attempt counter
        

        if user_input == word:
            correct_guess = True
            print(f"""
Congratulations! You guessed it!
It took you {guesses} guesses.
""")

        for i in range(len(word)):
            if user_input[i] in word:
                if user_input[i] == word[i]:
                    hints[i] = user_input[i].upper()
                else:
                    hints[i] = user_input[i].lower()
            else:
                hints[i] = "_ "

        print(f"Your hint is {''.join(hints).strip()}")

game()