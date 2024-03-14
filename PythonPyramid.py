class Function:

    @staticmethod
    def drawPyramid(num_rows):
        for i in range(num_rows):
            print(' ' * (num_rows - i - 1) + '*' * (2 * i + 1))
            
    @staticmethod
    def reversePyramid(r_rows):
        for i in range(r_rows, 0, -1):
            print(' ' * (r_rows - i) + '*' * (2 * i - 1))

class Input:
    
    def draw():
        print("\nWelcome to Duncan's Python Pyramid!\n")
        num_rows = int(input("Enter the number of rows in the pyramid: "))
        Function.drawPyramid(num_rows)
    
    def reverseDraw():
        print("\nWelcome to Duncan's reverse Pyramid!\n")
        r_rows = int(input("Enter the number of rows int the pyramid: "))
        Function.reversePyramid(r_rows)
        
    def selector():
        choice = str(input("Enter D to draw a pyramid, or enter R to draw a reverse pyramid: ")).upper()
        if choice == "D":
            Input.draw()
        elif choice == "R":
            Input.reverseDraw()
        else:
            print("Try again")
        
if __name__ == "__main__":
    Input.selector()