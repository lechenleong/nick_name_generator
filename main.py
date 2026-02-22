
print("Welcome to the Random Nickname Generator!\n\n" \
"In this website you will enter your first and last name. Then we will decide your nickname.\n" \
"You will then see your new nickname in the form below:\n" \
"First_name (nickname) Last_name\n" \
"Warning: most of the nicknames here are mean. Please enjoy!\n\n")


while True:
    first_name = input("What is your first name?  ")
    if any(char.isalpha() for char in first_name):
        break
    print("Please enter a valid name (must include letters).")

while True:
    last_name = input("What is your last name? ")
    if any(char.isalpha() for char in last_name):
        break
    print("Please enter a valid name (must include letters).")

gender = input("If you are a boy type 1 or if you are a girl type 2: ")
gender = int(gender)

if gender == 1:
    names = ['Chicken butt', 'Fish Head', 'Lion heart', 'The Eon','Bonehead', 'Knucklehead','Pea Brain','Trash panda','Buffoon', 'Butt head', 'Smelly sock', 'Buffon', 'Gay boy', 'Numb skull', 'Gay boy','Lag Machine', 'Noob Tube', ' Cereal Killer', 'Panic Button', 'Gay boy',' Chaos Goblin', 'Chicken head','Kenchinchin']
elif gender == 2:
    names = ['Dr. Doom-pa-Loompa', ' Cuddle Monster', 'Panic Button', 'Tater Tot','Slimy brain']
else:
    names = ["Liar pants on fire"]

import random



picked_name = random.choice(names)
# print(picked_name)

print(f"{first_name} {picked_name}  {last_name}")