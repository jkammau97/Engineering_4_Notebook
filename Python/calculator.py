
# Bob Kammauff
# Python Program 01 – Calculator (Hello Functions)

def doMath(x, y ,z):
    if z == 1:
        return x + y
    if z == 2:
        return x - y
    if z == 3:
        return x * y
    if z == 4:
        return x / y
    if z == 5:
        return x % y # % is modulo; gives the remainder of the two numbers when divided.

print("calculator Program")
print("enter your first number: ")
a = int(input()) #need to convert the input into a number so we can do stuff with it
print("enter your second number: ")
b = int(input()) #need to convert the input into a number so we can do stuff with it

print("Sum:\t\t" + str(doMath(a,b,1)))  #str() is needed because that's how it's gonna print it out
print("Difference:\t" + str(doMath(a,b,2)))
print("Product:\t" + str(doMath(a,b,3)))
print("Quotient:\t" + str(doMath(a,b,4)))
print("Modulo:\t\t" + str(doMath(a,b,5)))
