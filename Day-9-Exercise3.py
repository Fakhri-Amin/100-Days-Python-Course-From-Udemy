import os
# Blind Auction (Who bids the highset bid)

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bidding = {}
continue_bidding = True
print("Welcome, bid now!")


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for i in bidding_record:
        bid_amount = bidding_record[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of {highest_bid}")


while continue_bidding:
    os.system("cls")
    print(logo)
    person_name = input("What is your name? ")
    bid_price = int(input("What is your bid? "))

    bidding[person_name] = bid_price

    repeat = input("Are there any other bidders? Type 'yes' or 'no'")
    if repeat.lower() == "no":
        continue_bidding = False

find_highest_bidder(bidding)
