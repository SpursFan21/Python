while True:
    print("Welcome to Duncan's Silent Auction!")
    try:
        totalBidders = int(input("Enter the amount of bidders in the auction: "))
    except ValueError as e:
        print(f"Invalid input: {e}")

    bidders_dict = {}  # Dictionary to store bidder information

    while totalBidders > 0:
        try:
            bidder = str(input("Enter bidders name: ")).lower()
            bid = float(input("Enter your bid amount: "))
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue  # Restart the loop if there's an invalid input

        bidders_dict[bidder] = bid  # Add bidder and bid to the dictionary
        totalBidders -= 1
        print(f"Current bidders left {totalBidders}")
    
    print("Bidders and their bids:")
    for bidder, bid in bidders_dict.items():
        print(f"{bidder}: {bid}")
    
    if bidders_dict:  # Check if there are any bids before finding the winner
        winner = max(bidders_dict, key=bidders_dict.get)
        winning_bid = bidders_dict[winner]
        print(f"\nThe winner is {winner} with the highest bid of {winning_bid}!")
    
    user_choice = input("Do you want to encrypt or decrypt again? (yes/no): ").lower()
    if user_choice != 'yes':
        break