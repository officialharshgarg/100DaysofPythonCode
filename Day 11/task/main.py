import random
from art import logo
print(logo)
print("Game begins now, may the lucky one wins!")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game="on"
user=[]
computer=[]
u_score=0
c_score=0
while game != "off":
    user=random.choices(cards,k=2)
    computer=random.choices(cards,k=2)



