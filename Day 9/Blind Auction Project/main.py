# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
print("Welcome to auction of luxury")
bidding = "on"
bid={}
while bidding != "over":
    bidder=input("What's name of bidder?")
    amount=int(input("How much would you like to bid?"))
    bid[bidder]=amount
    more_bidders=(input("Are there more bidders? (yes/no)")).lower()
    if more_bidders == "no": bidding="over"
    else: print("\n"* 30)
max=0
winner=''
for key in bid:
     if bid[key] > max:
         max=bid[key]
         winner=key
print(f"Auction Won by {winner} with bid amount ${max}")