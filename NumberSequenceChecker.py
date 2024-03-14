class NumberChecker:
    def __init__(self, sequence):
        self.sequence = sequence

    def are_all_different(self):
        unique_numbers = set(self.sequence)
        return len(unique_numbers) == len(self.sequence)

if __name__ == "__main__":
    sequence = input("Enter a sequence of numbers separated by spaces: ").split()
    try:
        sequence = list(map(float, sequence))  # Convert input to list of floats
        number_checker = NumberChecker(sequence)
        if number_checker.are_all_different():
            print("All numbers in the sequence are different from each other.")
        else:
            print("Some numbers in the sequence are repeated.")
    except ValueError:
        print("Invalid input. Please enter a sequence of numbers separated by spaces.")
