''' This is a coding exercise from Chanpter 3 of Automate the Boring Stuff by Al Sweigart.
What this does is explore the COLLATZ SEQUNCE.

The idea is that this sequence will eventually evaluate to 1.
Mathematically:
f(n) = n/2 if n=0 (mod 2) # meaning if even
     = 3n+1 if n=1 (mod 2) # if odd
'''

def collatz(number):

    if number%2 == 0:  # EVEN number
        return number // 2

    else:  # ODD number
        return 3*number+1

try:
    inputNumber = int(input("Kindly enter a number: "))

    while inputNumber !=1:  # Compare first if the input is not 1 as we do not want to call collatz if its already 1.
        inputNumber = collatz(inputNumber)  # evaluate the collatz value for a given number and make that the new input.
        print(inputNumber)  # For checking that the collatz value being evaluated is correct,

except ValueError:
    print("Invalid argument.")  # Used to catch invalid input types (str or float)
