# Number guessing game using random function
# Author: Duncan

import random
import math

# taking inputs
lower = int(input("Enter Lowest number:- "))
upper = int(input("Enter Highest number:- "))

# generate random number between lower and upper
x = random.randint(lower, upper)

print("\n\tYou've only ",
    round(math.log(upper - lower + 1, 2)),
    " chances to guess the integer!\n")

# number of guesses.
count = 0

# for calc of min number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # taking guessing number input
    guess = int(input("Guess a number:- "))

    # condition
    if x == guess:
        print("Congradulations, you did it in ",
              count, "tries")
        break
    elif x > guess:
        print("Too Small!")
    elif x < guess:
        print("Too High!")

# if guessing is more than required guesses
    if count >= math.log(upper - lower + 1,2):
        print("\nThe number is %d" % x)
        print("\tBetter luck next time!")