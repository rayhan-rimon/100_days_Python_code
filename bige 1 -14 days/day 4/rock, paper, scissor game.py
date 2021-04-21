import random

# Rock Paper Scissors Game

# Rock '0'
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper '1'
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors '2'
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_list = [rock, paper, scissors]

user_choice = int(input('What do you choose? type 0 for Rock, 1 for paper or 2 for Scissors :\n'))


if user_choice >= 3 or user_choice < 0:
    print('You typed an invalid number. Please type a write number.')
else:
    print(f'User Choose: \n{game_list[user_choice]}')


computer_choice = random.randint(0, 2)
print(f'Computer choose: \n{game_list[computer_choice]}')



if user_choice == 0 and computer_choice == 2:
    print('You Win!')

elif computer_choice == 0 and user_choice == 2:
    print('You lose!')

elif user_choice > computer_choice:
    print('You Win!')

elif computer_choice > user_choice:
    print('You lose!')

elif computer_choice == user_choice:
    print("It's Draw!")
