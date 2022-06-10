# Imports the random module to make the game work.
import random

number = input("Kindly type a number for the upper range, number has to be higher than one: ")

# If statement that checks if the value that was put in is a digit
if number.isdigit():
    number = int(number)

# Else statement that will print out if the user inputs something other than a number higher than one.
else:
    print("You did not insert a number higher than one, kindly do this next time. Game over.")
    quit()

guess_number = random.randint(1, number)
attempts = 0

# While loop for the guessing part of the game.
while True:
    attempts += 1
    guess_user = input(f"Make your guess of the random number(between 1-{number}) here: ")
    if guess_user.isdigit():
        guess_user = int(guess_user)

# Else statement in case the user makes an error with the input.
    else:
        print("You have to guess a number, try again!")
        # This makes the loop continue so that the game wouldn't have to restart.
        continue

# If statement for when the user gets the correct number.
    if guess_user == guess_number:
        print("Great work, you guessed the right number!!")
        # This breaks the loop as the user has already won the game.
        break
    elif guess_user < guess_number:
        print("\nYour guess is too low. Try again and go a little higher!")
    else:
        print("\nYour guess is too high. Try again and go a little lower!")

# This prevents the issue of printing out "Completed in 1 guessES", to make the english correct,
if attempts == 1:
    print("It took you 1 attempt to guess the right number, great job!")
else:
    print("It took you", attempts, "attempts to guess the right number, great job!")
