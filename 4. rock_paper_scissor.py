import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_icon = [rock, paper, scissors]

user_input = input("What do you want to choose? Type 0 for Rock, 1 for Paper, or 2 for Scissor.\n")
print("\nYou chose" + list_icon[int(user_input)])

random_index = random.randint(0, 2)
print(f"Computer chose {list_icon[random_index]}")

if int(user_input) == random_index:
    print("It's a tie...")
elif int(user_input) == 0 and random_index == 1:
    print("You lose")
elif int(user_input) == 0 and random_index == 2:
    print("You win")
elif int(user_input) == 1 and random_index == 0:
    print("You win")
elif int(user_input) == 1 and random_index == 2:
    print("You loss")
elif int(user_input) == 2 and random_index == 0:
    print("You loss")
elif int(user_input) == 2 and random_index == 1:
    print("You win")
else:
    print("Invalid input. Please try again...")
