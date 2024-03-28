def main():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        result = num * i
        print(num, "x", i, " = ", result)
if __name__ == "__main__":
    main()