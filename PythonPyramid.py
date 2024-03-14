class Function:

    @staticmethod
    def draw_pyramid(rows):
        for i in range(rows):
            print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

class Input:
    
    def Draw():
        print("Welcome to Duncan's Python Pyramid\n")
        num_rows = int(input("Enter the number of rows in the pyramid: "))
        Function.draw_pyramid(num_rows)
        
if __name__ == "__main__":
    Input.Draw()