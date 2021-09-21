# Quadratic Solver

# Written By: Bob Kammauff
import math
from math import sqrt

def quadratic(x, y, z):
    d = x * y-(4*x*z) # "The function calculates the discriminant for the quadratic"
    # d is the discriminant
    
    if d < 0:
        print("no real roots")
        return None
        # "If the discriminant is negative, the user gets a message that there are no real roots"
    else:
        return [(-y + sqrt(d))/(2*x), (-y - sqrt(d))/(2*x)] 
        # "If the discriminant is zero or positive, the function returns an array of the two roots."
    
print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0")

while True:
    # find values for a b c
    print("what's a?")
    a = int(input())
    print("What's b?")
    b = int(input())
    print("What's c?")
    c = int(input())
    # "The program sends the three coefficients to a function"
    
    myList = [quadratic(a, b, c)]
    # "The program then prints the two roots.  This occurs outside of the function."
    print(myList)
    
    # After the roots are displayed, ask the user if they want to run another set of roots, or if they want to quit (this is similar to your previous assignment -- reuse that code!)
    print("press enter to run another set of roots, or x then enter to quit")
    user = input()
    if user == 'x':
        print("Goodbye!")
        break
    
