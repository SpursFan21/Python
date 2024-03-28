class FileManage:
    @staticmethod
    def readFile():
        with open("text example.txt", "r") as file:
            contents = file.read()
            print(contents)
    
    @staticmethod
    def appendFile():
        userInput = input("\nEnter your input to append to file: ")
        with open("text example.txt", "a") as file:
            file.write("\n" + userInput)
    
    @staticmethod
    def writeFile():
        userInput = input("\nEnter your input to write to file: ")
        with open("text example.txt", "w") as file:
            file.write(userInput)

if __name__ == "__main__":
    while True:
        choice = int(input("\nEnter 1 to Read file, 2 to Append file, 3 to Write file, or 4 to exit: "))
        if choice == 1:
            FileManage.readFile()
        elif choice == 2:        
            FileManage.appendFile()
            FileManage.readFile()  # Call readFile again to display the updated content
        elif choice == 3:
            FileManage.writeFile()
            FileManage.readFile()  # Call readFile again to display the content after writing
        elif choice == 4:
            break
        else:
            print("Invalid input. try again")
    
