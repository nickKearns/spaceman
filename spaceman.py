#Thank you to Ben Laferty for help
import random
def load_word():

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = list(random.choice(words_list))
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    counter = 0
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for i in secret_word:
        if i in letters_guessed:
            counter += 1
    if counter == len(secret_word):
        return True
    else:
        return False

def letter_already_guessed(user_guess, letters_guessed):
    if user_guess in letters_guessed:
        return True
    else:
        return False

        

def get_guessed_word(secret_word, letters_guessed):
     

    return_string = []
    for i in secret_word:
        if i in letters_guessed:
            return_string.append(i)
        else:
            return_string.append("_")
    return return_string
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet


def is_guess_in_word(guess, secret_word):
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False

    

def print_progress(secret_word, guessed_letters):
    print(''.join(get_guessed_word(secret_word, guessed_letters)))


def spaceman(secret_word):
   
    number_of_guesses = len(secret_word)
    guessed_letters = []
    #TODO: show the player information about the game according to the project spec

    cont = True
    while cont:
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        invalid_input = True
        while invalid_input:
            
            user_input = input("Please guess a letter.\n")
            if user_input.isalpha() == True and len(user_input) == 1 and not letter_already_guessed(user_input, guessed_letters):

                #checks that the inputed string is a letter and only 1 letter

                

                invalid_input = False
                
                guessed_letters.append(user_input)
            elif letter_already_guessed(user_input, guessed_letters):
                print("That letter has already been guessed!")
                invalid_input = True
            else:
                
                invalid_input = True
                print("invalid input try again")
        
        
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback


        #TODO: show the guessed word so far

        if is_guess_in_word(user_input, secret_word):

            # call get guessed word

            
            print("That is a correct guess!")
            print_progress(secret_word, guessed_letters)


        else:
            
            #increase number of wrong guesses and print the built string so far

            print("That letter is not in the word. Sorry")
            print_progress(secret_word, guessed_letters)
            number_of_guesses -= 1



            if number_of_guesses == 0:
                print("You have reached the maximum number of guesses, you lose.")
                print("The word was: " + secret_word + " .")
                cont = False
            print("You have: " + str(number_of_guesses) + " wrong guesses left.")
        if is_word_guessed(secret_word, guessed_letters) == True:
            print("You won the game!")
            cont = False








#These function calls that will start the game

secret_word = load_word()
print("This is a game of spaceman. You will guess the word letter by letter.")
#print(secret_word)


    
spaceman(secret_word)

