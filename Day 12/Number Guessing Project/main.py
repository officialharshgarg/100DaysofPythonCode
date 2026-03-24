import random
from art import logo
print(logo)
print("Welcome to number guessing game\nI'm thinking of number between 1 to 100.")

level=input("would you like easy or hard difficulty. Type 'easy' or 'hard'?")
num=random.randint(1,100)

def guess_num(num, g):
    limit = g+1
    print(f"You have got {g} guesses to find the correct number.")
    for n in range(1, limit):
        if n != limit:
                guess = int(input("Make a guess:"))
                if guess < num:
                    print("Your guess is too low.")
                elif guess > num:
                    print("Your guess is too high.")
                elif guess == num:
                    print("You guessed the correct number.")
        if n == g and guess != num:
            print("You ran out of guesses.")

if level == "easy":
    guess_num(num, 10)
elif level == "hard":
    guess_num(num, 5)