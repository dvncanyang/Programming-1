# Python Introduction
# Author: Duncan Yang
# Date: March 05, 2024

# Create a function called translate
# Translate RB
def translate(usr_input):
    return usr_input.replace("rb", " 🔴 𓃓  🏎")

# .
name = ""
fav_f1 = ""


# Greets the user
print("Good morning, Good evening, and Good night!")

# Asks the user's name
print("Whats your name?")
name = input()

# Ask them the F1 question with their name
print(f"So {name}, what's your favourite F1 team?")
fav_f1 = input().lower()

# Responds specifically to those questions
if fav_f1 == "red bull" or fav_f1 == "rb" or fav_f1 == "red-bull":
    print(translate("TUDUDUDU MAX VERSTAPPEN! rb"))
elif fav_f1 == "ferrari" or fav_f1 == "Ferrari":
    print("SMOOOTH OPERATORRRRR!")
elif fav_f1 == "mercedes" or fav_f1 == "Mercedes" or fav_f1 == "Benz" or fav_f1 == "benz":
    print("THROUGH GOES HAMILTON!!")
else:
    print("L choice!")

# Says goodbye using the user's name
print(f"Alright, it was nice meeting you, but I have to go watch Max Verstappen lap P11 again, peace {name}.")