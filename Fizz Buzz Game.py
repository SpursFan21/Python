while True:
    try:
        print("Welcome to Duncan's Fizz Buzz Game!")
        target = int(input("Enter your fizz buzz target number: "))
        for current in range(1, target + 1):
            if current % 3 == 0 and current % 5 == 0:
                print("Fizz Buzz")
            elif current % 3 == 0:
                print("Fizz")
            elif current % 5 == 0:
                print("Buzz")
            else:
                print(current)
        break
    except ValueError as e:
        print(f"Invalid input! {e} try again!")

    play_again = input("Do you want to play Fizz Buzz again? (yes/no): ").lower()
    if play_again != 'yes':
        break



