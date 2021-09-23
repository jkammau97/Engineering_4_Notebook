
def printHangman(triesNum):
    #---┐ 
    #   O 
    #  \|/
    #   | 
    #  / \
    print("---┐")
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

printHangman(0)
printHangman(1)
printHangman(2)
printHangman(3)
printHangman(4)
printHangman(5)
printHangman(6)
printHangman(7)