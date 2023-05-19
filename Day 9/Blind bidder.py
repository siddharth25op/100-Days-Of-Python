import art
import os
print(art.logo)

def highest_bid(bidding_dict):
    highest_number_bid = 0
    for bidder in bidding_dict:
            new_bid = bidding_dict[bidder]
            if new_bid > highest_number_bid:
                 highest_number_bid = new_bid
                 winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_number_bid}.")


should_end = False
bidding_dict = {}
while not should_end:
    name = input("Enter your name for bid: ")
    price = int(input("Enter the price for bid: $"))
    bidding_dict[name] = price
    os.system('clear')
    any_users = input("Are there an other users left for bid?: ").lower()
    if any_users == "no":
        should_end = True
        highest_bid(bidding_dict)
