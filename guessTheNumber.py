# This is a guess the number game
import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20")

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):  # range(1, 7) basically states take 6 guesses
    guess = int(input("Take a guess: "))
    guessesTaken += 1
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # This means that the correct guess has been given

    # Checks if the guess is the secretNumber
if guess == secretNumber:
    print("Good job! You guessed my number in {} guesses!"
          "\nThe correct number was {}.".format(guessesTaken, secretNumber))
else:
    print("Nope. The number I was thinking off was {}.".format(secretNumber))


