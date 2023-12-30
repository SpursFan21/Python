while True:
    print("Welcome to Duncan's high score finder!")

    # Input scores
    while True:
        scores_input = input("Enter all the scores separated by a space: ")
        try:
            # Convert input to a list of integers
            score_list = [int(score) for score in scores_input.split()]

            # Check if the list is not empty
            if not score_list:
                raise ValueError("Empty list, please enter at least one score.")

            # Initialize high score with the first score
            high_score = score_list[0]

            # Iterate through the scores to find the maximum
            for score in score_list:
                if score > high_score:
                    high_score = score

            # Calculate the number of scores
            num_scores = len(score_list)

            # Break out of the input loop
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again!")

    print(f"The high score is: {high_score}")
    print(f"The number of scores is: {num_scores}")

    # Ask if the user wants to try again
    play_again = input("Do you want to find the high score again? (yes/no): ").lower()
    if play_again != 'yes':
        break
