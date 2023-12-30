while True:
    try:
        print("Welcome to Duncan's even number calculator!")
        target = int(input("Enter a number: "))
        total = 0

        for number in range(2, target + 1, 2):
            total += number

        print(f"The sum of even numbers from 2 to {target} is: {total}")
        
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != 'yes':
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

