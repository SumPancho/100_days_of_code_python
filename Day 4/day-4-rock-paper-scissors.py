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

#Write your code below this line 👇

import random

choices = [rock, paper, scissors]

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

computer_choice = random.randint(0, 2)

if int(player_choice)>=3 or int(player_choice)<0:
  print("You inputted a wrong number. You Lose!")
else:
  print(choices[int(player_choice)])
  print("Computer choice:")
  print(choices[computer_choice])
  
  comparison = [int(player_choice), computer_choice]
  
  if comparison[0] == 0 and comparison[1] == 0:  
    print("Draw")
  elif comparison[0] == 0 and comparison[1] == 1:
    print("You Lose")
  elif comparison[0] == 0 and comparison[1] == 2:
    print("You Win")
  elif comparison[0] == 1 and comparison[1] == 0:
    print("You Win")
  elif comparison[0] == 1 and comparison[1] == 1:
    print("Draw")
  elif comparison[0] == 1 and comparison[1] == 2:
    print("You Lose")
  elif comparison[0] == 2 and comparison[1] == 0:
    print("You Lose")
  elif comparison[0] == 2 and comparison[1] == 1:
    print("You Win")
  else:
    print("Draw")
  
