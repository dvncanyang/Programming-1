# Python Introduction
# Author: Duncan Yang
# Date: 13 February 2024

# .
name = ""
age = ""
fav_car = ""
fav_class = ""

# Greets the user
print("Good morning, Good evening, and Good night!")

# Asks the user's name
print("Whats your name?")
name = input()

# Ask them 1st question
print(f"How old are you, {name}?")
age = input()

# Responds specifically to those questionsDun
print(f"Oh nice! {age} is pretty young! I'm actually ancient compared to you!")

# Ask them 2nd question
print(f"Whats your favourite car, {name}?")
fav_car = input()

# Responds specifically to those questions
if fav_car == "Nissan GTR R34":
    print("TWINSIES 🤭")
else:
    print(f"COOL! Mine is Nissan GTR R34, but {fav_car} would be in my top 5 fosho.")

# Ask them 3rd question
print(f"So {name}, what's your favourite class?")
fav_class = input()

# Responds specifically to those questions
if fav_class == "Science":
    print("NERDDD 😒")
elif fav_class == "Computer Science":
    print("TWINSIES 🤭")
elif fav_class == "Programming":
    print("TWINSIES 🤭")
else:
    print("So basic 🙄.")

# Says goodbye using the user's name
print(f"Alright, it was nice meeting you, but I have to get going {name}, peace.")