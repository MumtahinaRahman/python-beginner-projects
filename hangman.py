import random
import word
import string

key_words = word.words


# this filters out words containing - or space
def find_valid_word(key_words):
    puzzle = random.choice(key_words)
    while('-' in puzzle) or (' ' in puzzle):
        puzzle = random.choice(key_words)
    return puzzle.upper()

# need to track which words have been used in a game
# which words have been correctly guessed
# which words were wrong
# which letters of the alphabet were used
# a major error in this program is that it cannot handle 'cannot' - words with repeating letters


def hangman():
    secret_word = find_valid_word(key_words)
    letters_in_current_word = set(secret_word)
    alphabet = set(string.ascii_uppercase)
    letters_already_used = set()  # letters used from the alphabet
    lives = 5

    while len(letters_in_current_word) > 0 and lives > 0:
        print(" ")
        print(f"you have {lives} lives left")
        print("you have used these letters: ", " ".join(letters_already_used))  # learn more about .join
        word_hint = [i if i in letters_already_used else '_' for i in secret_word]  # list comprehension
        print("current word: ", " ".join(word_hint))

        # getting user input
        user_input = input("guess a letter: ").upper()

        # if user input hasn't been used yet, add it to used letters
        if user_input in alphabet - letters_already_used:
            letters_already_used.add(user_input)
            if user_input in secret_word:
                letters_in_current_word.remove(user_input)
            else:
                lives = lives - 1
                print(f"sorry! {user_input} is not in the word")
        elif user_input in letters_already_used:
            lives = lives - 1
            print(f"sorry! you've already used {user_input}")
        # if anything but letters are pressed
        else:
            print("invalid input... try again")

        if lives == 0:
            print("oops! you have used all your lives!!")
            print(f"the word was {secret_word}")

        if letters_in_current_word == 0:
            print(f"woohoo! you guessed the word : {secret_word}")


hangman()
