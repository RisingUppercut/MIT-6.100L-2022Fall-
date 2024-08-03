# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True
   


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = ''
    for c in secret_word:
        if c in letters_guessed:
            guessed += c
        else:
            guessed += '*'
    return guessed


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase
    notbeen_guessed = ''
    for c in letters:
        if c not in letters_guessed:
            notbeen_guessed += c
    return notbeen_guessed
    
def is_valid(user_input, with_help):
    if with_help:
        return user_input.isalpha() or user_input == '!'
    else:
        return user_input.isalpha()
    

def get_help(secret_word, available_letters):
    all_letters = string.ascii_lowercase
    choose_from = ''
    for c in all_letters:
        if c in secret_word and c in available_letters:
            choose_from += c
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter

def count_unique(secret_word):
    unique_letters = ''
    for c in secret_word:
        if c not in unique_letters:
            unique_letters += c
    return len(unique_letters)

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.
     
    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remain = 10
    letters_guessed = ''
    won = True
    
    print('Welcome to Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    
    while guesses_remain > 0 and get_word_progress(secret_word, letters_guessed) != secret_word:
        print('--------------')
        print(f'You have {guesses_remain} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        user_input = input('Please guess a letter: ')
        if user_input.isalpha():
            user_input = user_input.lower()
        if not is_valid(user_input, with_help):
            print('Oops! That is not a valid letter. Please input a letter from the alphabet: ', end = '')
        else:   # is valid input
            if user_input == '!':
                if guesses_remain < 3:
                    print('Oops! Not enough guesses left: ')
                else:
                    guesses_remain -= 3
                    available_letters = get_available_letters(letters_guessed)
                    revealed_letter = get_help(secret_word, available_letters)
                    letters_guessed += revealed_letter
                    print(f'Letter revealed: {revealed_letter}')
                    
            else:
                if user_input in letters_guessed:  #guessed before
                    print('Oops! You\'ve already guessed that letter: ', end = '')
                else:   #havent been guessed
                    letters_guessed += user_input
                    if user_input in secret_word:
                        print('Good guess: ', end = '')
                    else:
                        if user_input in 'aeiou':
                            if guesses_remain < 2:
                                won = False
                                break
                            guesses_remain -= 2
                        else:
                            guesses_remain -= 1
                        print('Oops! That letter is not in my word: ', end = '')
        print(get_word_progress(secret_word, letters_guessed))
            
    if get_word_progress(secret_word, letters_guessed) == secret_word:
        won = True
    else:
        won = False
    print('--------------')
    
    if won:
        total_score = guesses_remain + 4*count_unique(secret_word) + 3*len(secret_word)
        print('Congratulations, you won!')    
        print(f'Your total score for this game is: {total_score}')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
           



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = 'wildcard'
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

