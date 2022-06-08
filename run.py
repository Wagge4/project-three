# Imports the random module to make the game work.
import random

number = input("Kindly type a number higher than 1, for the upper range: ")

# If statement that checks if the value that was put in is a digit
if number.isdigit():
    number = int(number)

else:
    print("You did not insert a number higher than 1, kindly do this next time. Game over.")
    quit() 

guess_number = random.randint(1, number)
attempts = 0
