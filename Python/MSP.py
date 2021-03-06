# Man-Shaped Pinata
# Bob Kammauff
# 9/30/2021
def printHangman(triesNum): #program that prints out a man if there's an incorrect guess
    #---┐ 
    #   O 
    #  \|/
    #   | 
    #  / \
    print("---┐")
    if triesNum == 0:
        print('\n'*4) #prints space for hangman to exist
    if triesNum == 1:
        print("   O ")
        print("     ")
        print("     ")
        print("     ")
    if triesNum == 2:
        print("   O ")
        print("   | ")
        print("     ")
        print("     ")
    if triesNum == 3:
        print("   O ")
        print("   | ")
        print("   | ")
        print("     ")
    if triesNum == 4:
        print("   O ")
        print("   | ")
        print("   | ")
        print("    \\")
    if triesNum == 5:
        print("   O ")
        print("   | ")
        print("   | ")
        print("  / \\")
    if triesNum == 6:
        print("   O ")
        print("   |/")
        print("   | ")
        print("  / \\")
    if triesNum == 7:
        print("   O ")
        print("  \|/")
        print("   | ")
        print("  / \\")

letters = "abcdefghijklmnopqrstuvwxyz"
#Beginning
while True:
    boolToBreak = False #if set to true, it will go back to the beginning
    print("Man-Shaped Pinata by Bob Kammauff")
    print("Player 1, Enter a word:")
    word = input() #get string of word
    word = word.casefold()
    for x in word:
            if x not in letters and x not in " .!?,-" :
                print("bad word, try again")
                boolToBreak = True #if set to true, it will go back to the beginning
                break
    if boolToBreak == True: #so that it can request another entry nbecause the person put a stupid one
        continue
    #word = "pineapple" #for debugging; I don't wanna enter the word every time
    print('\n' * 50)
    
    print("cleared screen! don't scroll up!")

    badGuesses = {'value'} # Using a python set because they are unordered, and do not accept duplicates
    badGuesses.remove('value')
    answerList = [] # make a list for what player 2 has for the answer so far
    
    for x in word:
        answerList.append('_ ')
    #gives spaces and other common non-letters as givens
    givens = (' ', '-', '.', '?', '!', ',') #this is a tuple; ordered and unchanging
    for x in givens:
        if x in word:
            i = word.find(x)
            while i > -1:
                answerList[i] = x + " "
                i = word.find(x, i+1)
    while True:
        printHangman(len(badGuesses)) 
        print("Missed Guesses: " + str(badGuesses))
        if len(badGuesses) >= 7:
            print("you LOSE!")
            break
        answer = ""
        for x in answerList:
            answer = answer + x
        print(answer)
        
        if '_ ' not in answerList:
            print("you win!")
            break
        
        guess = input("Player 2, guess a letter: ")
        guess = guess.casefold() #make everything lower case so that it works
        
        # the idea here is that we check if the character is in the word, then finds the position of the character in the word, which corresponds to that position in the list
        # change the "_ " to the character to reveal it, then loop back to the Beginning
        
        if len(guess) > 1 or guess not in letters:
            print("don't guess multiple letters or non-letters thats above my pay grade")
            continue
        if guess in word:
            i = word.find(guess)
            while i > -1:
                answerList[i] = guess + " "
                i = word.find(guess, i+1)
        else:
            badGuesses.add(guess)
    print("The correct answer was: " + word)
    if input("press y then enter to play again") != 'y':
        print("exiting program...")
        break
        
