import random
from art import logo

print(logo)
print("Game begins now, may the lucky one win!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def total_score(hand):
    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def play_game():
    user = [deal_card(), deal_card()]
    computer = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = total_score(user)
        comp_score = total_score(computer)

        print(f"\nYour cards: {user}, score: {user_score}")
        print(f"Computer's first card: {computer[0]}")

        if user_score > 21:
            print("You went over. You lose 😢")
            return

        choice = input("Type 'y' to get another card or 'n' to pass: ")

        if choice == 'y':
            user.append(deal_card())
        else:
            game_over = True

    # Computer's turn
    while total_score(computer) < 17:
        computer.append(deal_card())

    user_score = total_score(user)
    comp_score = total_score(computer)

    print(f"\nFinal hands:")
    print(f"Your cards: {user}, score: {user_score}")
    print(f"Computer's cards: {computer}, score: {comp_score}")

    if comp_score > 21 or user_score > comp_score:
        print("You win! 🎉")
    elif user_score < comp_score:
        print("Computer wins! 🤖")
    else:
        print("It's a draw!")

# Run game
play_game()