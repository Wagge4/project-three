# Imports the random module to make the game work.
import random

number = input("Kindly type a number for the upper range, number has to be higher than one: ")

# If statement that checks if the value that was put in is a digit
if number.isdigit():
    number = int(number)

# Else statement that will print out if the user inputs something other than a number higher than 1
else:
    print("You did not insert a number higher than 1, kindly do this next time. Game over.")
    quit()

guess_number = random.randint(1, number)
attempts = 0

# While loop for the guessing part of the game
while True:
    attempts += 1
    guess_user = input(f"Make your guess of the random number(between 1-{number}) here: ")
    if guess_user.isdigit():
        guess_user = int(guess_user)
# Else statement in case the user makes an error with the input.
    else:
        print("You have to guess a number, try again!")
        continue
