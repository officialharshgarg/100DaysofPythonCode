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
moves = [rock, paper, scissors]
user=int(input("What do you choose? 0: Rock, 1: Paper, 2: Scissors "))
comp=random.randint(0,2)
if user >= 3 or user < 0:
    print("invalid input")
elif comp==user:
    print(f"You chose {moves[user]} and {moves[comp]}\nDraw!")
elif comp ==0 and user==1:
    print(f"You chose {moves[user]} and captures {moves[comp]}\nYou win!")
elif comp ==1 and user==2:
    print(f"You chose {moves[user]} and scissors {moves[comp]}\nYou win!")
elif comp ==2 and user==0:
    print(f"You chose {moves[user]} and crushes {moves[comp]}\nYou win!")
elif comp ==2 and user==1:
    print(f"you chose {moves[user]} and computer chose {moves[comp]}\nYou lose!")
elif comp ==0 and user==2:
    print(f"you chose {moves[user]} and computer chose {moves[comp]}\nYou lose!")
elif comp ==1 and user==0:
    print(f"you chose {moves[user]} and computer chose {moves[comp]}\nYou lose!")
