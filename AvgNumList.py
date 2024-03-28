def main():
    num_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    average = sum(num_list) / len(num_list)
    print(f"The average is {average}")
    
if __name__ == "__main__":
    main()
