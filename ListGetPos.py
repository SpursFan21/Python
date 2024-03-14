class Data:
    color_list = ["Red", "Green", "White", "Black"]
    
    def getPos(color_list):
        print("Welcome to Duncan's List Get Postion\n")
        get_pos = int(input("Enter the position of this list to view its contents: "))
        print((color_list[get_pos]))

if __name__ == "__main__":
    Data.getPos(Data.color_list)