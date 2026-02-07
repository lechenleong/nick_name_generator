
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

import random

names = ['chicken', 'Fish Head', 'lion heart', 'the eon','Bonehead', 'Knucklehead','Pea Brain','Tater Tot','Trash panda','Buffoon', 'Butt head']

picked_name = random.choice(names)
# print(picked_name)

print(f"{first_name} {picked_name}  {last_name}")