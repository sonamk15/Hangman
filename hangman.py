import string
from words import choose_word
from images import IMAGES
import random
# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word == get_available_letters(letters_guessed):
        return True
    else:    
        return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    all_letters = string.ascii_lowercase
    letters_left = ""
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    return letters_left

def ifAlphaValid(user_alpha):
    if len(user_alpha) == 1:
        if user_alpha.isalpha():
            return True
    return False

def get_hint(secret_word, letters_guessed):
    letters_user_not_guess = []
    for i in secret_word:
        letter = secret_word[i]
        if letter in letters_guessed:
            if letter in letters_user_not_guess:
                i += 1
        else:
            letters_user_not_guess.append(letter)
    return random.random(letters_user_not_guess)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""

    total_lives = user_lives = 8
    user_choosing_difficulty = raw_input("Choose your level, which level you want to play\na) Easy\nb) Mediume\nc) Hard\n write your answer in a,b,c")
    images_selection_list = [0, 1, 2, 3, 4, 5, 6, 7]
    if user_choosing_difficulty == "c":
        total_lives = user_lives = 8

    elif user_choosing_difficulty == "b":
        total_lives = user_lives = 6
        images_selection_list = [0, 2, 3, 5, 6, 7]

    elif user_choosing_difficulty == "a":
        total_lives = user_lives = 4
        images_selection_list = [0, 3, 5, 7]
    else: 
        print "Aapki choice invalid hai.\nGame easy mode mei start kar rahe hai\n"


    letters_guessed = []

    user_lives = 8
    while total_lives > 0:
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " , available_letters

        guess = raw_input("Please guess a letter: ")

        if guess == "hint":
            letter = get_hint(secret_word, letters_guessed)
        elif guess in letters_guessed:
            print "You have to choose other alphabate for guessing a word"
        else:    
            letter = guess.lower()
            
            ''' if we put (letter = guess.lower()) after if than it will show an error "UnboundLocalError: local variable 'letter' referenced before assignment" '''
            
            if (not ifAlphaValid(letter)):
                continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print " "

        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            print IMAGES[images_selection_list[user_lives - total_lives ]]
            total_lives -= 1
    
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)