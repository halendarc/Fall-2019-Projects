while True:

    def reset():
        global phrase #the phrase to be entered for the game, convert to list and back
        global guess #the guess - user input
        global remaining #the number of guesses for the game, decreases with each unique, non-repeated guess
        global used #the selection of letters that have been guessed
        global board #the game board, convert to list and back
        global multiple #List, used to store the indices of found letters to pass on to update_board()
        
        phrase = " "
        guess = " "
        remaining = 1
        used = [ ]
        board = "-"
        multiple = [ ]

    def what_is_global():
        global remaining
        global used
        remaining = str(remaining)
        used = str(used)
        print("phrase is: " + phrase)
        print("guess is: " + guess)
        print("remaining is: " + remaining)
        print("used_letters is: " + used)
        print ("board is: " + board)

    def create_board():
        global board
        i = 0
        for i in range(0, len(phrase)-1): #creates a blank board
            if phrase[i+1] != " ":
                board = board + "-" #every value that isn't a space becomes a hyphen
            elif phrase[i+1] == " ":
                board = board + " "#every value that is a space bceomes a space

    def guess_letter(x): 
        global remaining
        global used
        x = x.upper()
        print("You guessed: " + x + "\n")
        if if_used(x) == True: #checks if the letter has already been used or not 
            print("You already tried that letter!")
        elif search_phrase(x) == False: #checks if the letter is in the phrase or not
            print("Oh no! " + x + " isn't in this phrase.")
            remaining = remaining - 1
            used.append(x) #adds the letter to the list of used letters
        elif search_phrase(x) == True: #checks if the letter is in the phrase or not 
            used.append(x) #adds the letter to the list of used letters
            count_phrase(x) #checks to see how many times the letter appears
            update_board(x) #updates the playing board by filling in the spaces where the letter appears

    def if_used(x):
        global remaining
        global used
        if (x in used):
            return True

    def search_phrase(x):
        i = 0
        for i in range(0, len(phrase)):
            if (x in phrase):
                return True
            else:
                return False
                
    def count_phrase(x):
        if search_phrase(x) == True: #double checks to see if the letter is in the string 'phrase'
            i = 0
            m = 0
            global multiple
            multiple = [ ]
            while i < len(phrase): 
                if phrase[i] == x: #checks to see the value of the location where the letter is, as many times as it shows up
                    multiple.append(i) #adds the value of the location to a list
                i += 1

    def update_board(x):
        global board
        global multiple
        i = 0 
        board = list(board) #typecasts 'board' as a mutable list
        while i < len(multiple):
            board[multiple[i]] = x #pulls the location of the letter in 'phrase' from the list and adds it to the same index in 'board'
            i += 1
        board = "".join(board) #joins 'board' back together
        board = str(board) #doublecheck; typecasts 'board' as a string again
        print(board)
        print("\n")
        if board == phrase:
            print("Congratulations! You did it!")
            exit()       

    reset()
    phrase = input("Enter a Word for Hangman: ")
    phrase = phrase.upper()
    remaining = input("Number of wrong answers allowed: ")
    remaining = int(remaining)
    create_board()
    print(board)

    while remaining > 0:    
        x = input("Guess a letter: ")
        guess_letter(x)
        print (remaining, end=" ")
        print ("strikes left!")
        print (used)
        print ("____________________________________\n")

    print("Better luck next time!\n")

