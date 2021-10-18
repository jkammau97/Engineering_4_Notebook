# Engineering_4_Notebook
Engineering Notebook for 2021-22 school year
<details>
  
  windows+shift+'s' to screenshot
  
  <img src= "https://i2.wp.com/creapills.com/wp-content/uploads/2018/03/30-photos-absurdes-banques-dimages-23.jpg?resize=800%2C536&ssl=1" alt="Me when I use toilet paper rolls as binoculars" width="1000" height="70">
  
  I didn't ask you to document hello_world.py or dice_roller.py. I'll start off with an example for dice_roller.py, and then you will reflect on calculator.py.

</details>
  
## Table of Contents
* [Python_Calculator](#Python_Calculator)
* [Quadratic_Solver](#Quadratic_Solver)
* [Strings_and_Loops](#Strings_and_Loops)
* [MSP](#MSP)
---

## Python_Calculator

### Assignment Description

> Write a python_calculator.py program that gives you the sum, difference, quotient, and modulo of the two numbers.  The program asks the user for two numbers and then runs them through one function, five different times.  The last five lines of the program should look something like this:
> 
> ```python3
> print("Sum:\t\t" + doMath(a,b,1))
> print("Difference:\t" + doMath(a,b,2))
> print("Product:\t" + doMath(a,b,3))
> print("Quotient:\t" + doMath(a,b,4))
> print("Modulo:\t\t" + doMath(a,b,5))
> ```

Math has to be done within ONE function called `doMath(x, y, z)`
### Evidence 
Vanilla version:

[<img src="Media/calculator.PNG" alt="calculator.PNG" width="" height="">](Python/calculator.py)

Spicy version:

[<img src="Media/calculator_spicy.PNG" alt="calculator_spicy.PNG" width="" height="">](Python/calculator_spicy.py)

### Wiring
N/A

### Reflection

Had a very easy time figuring this out. The function simply returns the result based upon what number is inputted for `z`. Converting the input into an integer is important so that it doesn't crash. I already knew that `%` was the modulo sign. The spicy version returns the factorials of both numbers as well.

## Quadratic_Solver

### Assignment Description

> Requirements for the program.  Read carefully:
> 
> The program sends the three coefficients to a function 
> The function calculates the discriminant for the quadratic
> If the discriminant is negative, the user gets a message that there are no real roots
> If the discriminant is zero or positive, the function returns an array of the two roots.  The program then prints the two roots.  This occurs outside of the function.
> After the roots are displayed, ask the user if they want to run another set of roots, or if they want to quit (this is similar to your previous assignment -- reuse that code!)

### Evidence 

[<img src="Media/Quadratic.png" alt="Quadratic.png" width="" height="">](Python/quadratic_solver.py)

### Wiring

N/A

### Reflection

Had to remind myself how lists work in python. I don't like how it outputs the brackets as well, but it's not a big deal so there's no reason to change it. I also had a problem where the variables were strings instead of integers. Just had to convert the inputs to ints using `int()`.

## Strings_and_Loops 

### Assignment Description

> Write a program that asks the user to type a simple sentence.  The program then takes that sentence and splits it (using the split() function) into an array of words.  The program then loops through that array of words using a for loop.  For each word, the program then loops through the letters in the word (another for loop) and prints them to the screen.  At the end of each word, the program prints a minus sign.
> 
> Spicy Version (Optional):
> No additional requirements, but try to collapse your code into as few lines as possible (other than commented intro lines). You probably want to get your code working first, then look for ways to combine lines where possible. Mr. Miller's code is 4 lines long. Try to tie or beat that!
> 
> Note: Writing code into as few lines as possible isn't always good for code readability. In real life, you want to find a balance between being concise but understandable for other coders. For now though, this is a good challenge!

### Evidence 

[<img src="Media/strings_and_loops.png" alt="strings_and_loops.png" width="" height="">](Python/strings_and_loops_spicy.py)

### Wiring

N/A

### Reflection

More review. I just stole the concept for my code from [W3schools](https://www.w3schools.com/python/trypython.asp?filename=demo_for_string). It's crazy to me that it works like that, but idk if that concept works for all arrays (future me has come back to say that it doesn't work like I thought it would :/ ) I didn't use `string.split()` like it said to in the assignment description because I found that it was unnessesary, especially for trying to cut down the amount of lines on the code.

## MSP

(Man-Shaped Piñata)

### Assignment Description

Write code for a Hangman Game.

### Evidence 

[Link](Python/MSP.py)

```
Man-Shaped Pinata by Bob Kammauff
Player 1, Enter a word:
www.github.com

...

cleared screen! don't scroll up!
---┐





Missed Guesses: set()
_ _ _ . _ _ _ _ _ _ . _ _ _ 
Player 2, guess a letter: 
w
---┐





Missed Guesses: set()
w w w . _ _ _ _ _ _ . _ _ _ 
Player 2, guess a letter: 
ww
don't guess multiple letters or non-letters thats above my pay grade
---┐





Missed Guesses: set()
w w w . _ _ _ _ _ _ . _ _ _ 
Player 2, guess a letter: 
g
---┐





Missed Guesses: set()
w w w . g _ _ _ _ _ . _ _ _ 
Player 2, guess a letter: 
i
---┐





Missed Guesses: set()
w w w . g i _ _ _ _ . _ _ _ 
Player 2, guess a letter: 
t
---┐





Missed Guesses: set()
w w w . g i t _ _ _ . _ _ _ 
Player 2, guess a letter: 
h
---┐





Missed Guesses: set()
w w w . g i t h _ _ . _ _ _ 
Player 2, guess a letter: 
u
---┐





Missed Guesses: set()
w w w . g i t h u _ . _ _ _ 
Player 2, guess a letter: 
b
---┐





Missed Guesses: set()
w w w . g i t h u b . _ _ _ 
Player 2, guess a letter: 
c
---┐





Missed Guesses: set()
w w w . g i t h u b . c _ _ 
Player 2, guess a letter: 
o
---┐





Missed Guesses: set()
w w w . g i t h u b . c o _ 
Player 2, guess a letter: 
m
---┐





Missed Guesses: set()
w w w . g i t h u b . c o m 
you win!
The correct answer was: www.github.com
press y then enter to play again
```

### Wiring

N/A

### Reflection

Had to learn about all the different types of arrays that python uses and what they're good for. using a set for missed guesses gives it built-in ignoring guesses already made.

I was also having trouble because I accidentaly created an infinite `While` loop and it was causing the IDE to glitch and get stuck after the "guess a letter". It was confusing because it was making simple print functions not output anything, so I was stuck debugging for a while. Thankfully I figured out I forgot to add 1.


