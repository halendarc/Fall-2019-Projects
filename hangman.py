#while True:

def create_board(phrase):
    global g_board
    i= 0
    g_board = ""
    g_board = str(g_board)
    for i in range(0, len(phrase)):
        #print ("_ \r")
        g_board = g_board + "_ "
    print(g_board)
    return g_board


def guess_letter(phrase, guesses, used_letters, board):
    global g_guesses
    global g_used_letters
    global g_board
    board = g_board
    guesses = g_guesses
    guessed_letter = input("Guess a letter: ")
    guessed_letter = str(guessed_letter)
    if check_if_used(guessed_letter, used_letters) == True:
        print("Sorry, that letter has already been used.")
    else:
        guesses = guesses - 1
        g_guesses = guesses
    update_board(guessed_letter, phrase, board, used_letters)
    print("Guesses remaining: " + str(guesses))
    print("Guessed letters: \n")
    g_used_letters = used_letters
    print(g_used_letters)

def check_if_used(guessed_letter, used_letters):
    i = 0
    for i in used_letters:
        if (guessed_letter in used_letters):
            return True
        else:
            return False

def update_board(guessed_letter, phrase, board, used_letters):
    global g_board
    if search_phrase(guessed_letter, phrase) == True:
        i = find_letter(guessed_letter, phrase)     #i is assigned returned value of the location of the letter in the phrase

        L = list(board)     #turns the string 'board' into a list 
        L[i] = guessed_letter   #assigns the letter to the appropriate slot in the list 
        board = "".join(L)  #turns the list back into a string

        g_board = board #globalize variable 
        print(g_board)

    elif search_phrase(guessed_letter, phrase) == False:
        print("Sorry, that letter isnt in the phrase.")

def split(x):
    return list(x)
        

def search_phrase(guessed_letter, phrase): ##Needs to be FINISHED, but searches as it should, will need to call function to update board
    i = 0 
    for i in range(0, len(phrase)): #Start of Search
        if (guessed_letter in phrase):
            return True
        else:
            return False

def find_letter(guessed_letter, phrase):
    i = 0 
    for i in range(0, len(phrase)):
        if guessed_letter == phrase[i]:
            return i
        else:
            continue
                     
        
global g_phrase
global g_guesses
global g_used_letters
global g_board

g_phrase = input("Enter a word for Hangman: ")
g_phrase = str(g_phrase)
g_guesses = input("How many guesses?: ")
g_guesses = int(g_guesses)
g_used_letters = []
g_board = ""

create_board(g_phrase)

while g_guesses > 0:
    guess_letter(g_phrase, g_guesses, g_used_letters, g_board)
