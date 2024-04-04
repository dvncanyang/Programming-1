# Python Introduction
# Author: Duncan Yang
# Date: 20 February 2024

# make a bot that says yes only to different variations of 42

# ask the prompt
# if statements
# type response for each solution under each if statements

# askking the prompt
answer = (input("What is the answer to the ultimate question? Of life, universe, and everything?\n"))

# if condition
if answer == "42" or answer == "forty two" or answer == "forty-two":
    print("yes")

else:
    print("no")