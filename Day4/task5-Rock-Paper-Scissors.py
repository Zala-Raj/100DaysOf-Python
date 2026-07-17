'''
Task-5: Rock Paper Scissors

You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.
'''

import random

# ascii art of rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ascii art of paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# ascii art of scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose:")
print(game_images[computer_choice])

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif computer_choice < user_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("It's a draw!")

'''
Demo
https://appbrewery.github.io/python-day4-demo/
'''