
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

#Beginning

print("Man-Shaped Pinata")
print("Player 1, Enter a word:")
# word = input() #get string of word
word = "pineapple" #for debugging; I don't wanna enter the word every time
print('\n' * 50)

print("cleared screen! don't scroll up!")

badGuesses = {} # Using a python set because they are unordered, and do not accept duplicates

answerList = [] # make a list for what player 2 has for the answer so far

for x in word:
    answerList.append('_ ')

while True:
    printHangman(len(badGuesses))
    answer = ""
    for x in answerList:
        answer = answer + x
    print(answer)

    print("Player 2, guess a letter:")

    guess = input()
    # the idea here is that we check if the character is in the word, then finds the position of the character in the word, which corresponds to that position in the list
    # change the "_ " to the character to reveal it, then loop back to the Beginning
    if guess in word:
        i = word.find(guess)
        while i > -1:
            answerList[i] = guess + " "
            i = word.find(guess)

