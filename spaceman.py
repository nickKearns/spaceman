import random
running = True
guessed_letters = list()
number_of_guesses = 0
def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    if secret_word.lower() == letters_guessed.lower():
        return True
        print("word is guessed")
        print(secret_word)
        print(letters_guessed)
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''



    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False

    




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    #TODO: show the player information about the game according to the project spec

    print("This is a game of spaceman. You will guess the word letter by letter.")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    invalid_input = True
    while invalid_input:
        print("Please guess a letter.")
        user_answer = input()
        if user_answer.isalpha() == True and len(user_answer) == 1 and user_answer not in guessed_letters:
            invalid_input = False
        else:
            invalid_input = True
            print("invalid input try again")
    
    
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback


    #TODO: show the guessed word so far

    if is_guess_in_word:
        # call get guessed word


    #TODO: check if the game has been won or lost

        if is_word_guessed:
            print("you won the game! Would you like to play again? (y/n)")
            user_answer = input()
            if user_answer == "y":
                running = True
            elif user_answer == "n":
                running = False
            else:
                print("Please enter y or n")
                user_answer = "y"
        else:
            running=False







#These function calls that will start the game

while running:

    secret_word = load_word()
    spaceman(secret_word)
    print(secret_word)
