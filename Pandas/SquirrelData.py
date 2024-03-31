import pandas

class CSVManager:
    def getSquirrelFur():
        data = pandas.read_csv("./Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240401.csv")
        gray_squirrel = 0
        black_squirrel = 0
        cinnamon_squirrel = 0
        
        for color in data["Primary Fur Color"]:# counting squirrel fur colors
            if color == "Gray":
                gray_squirrel += 1
            if color == "Black":
                black_squirrel += 1
            if color == "Cinnamon":
                cinnamon_squirrel +=1

        squirrelFurColorCounts = {# storing data in dict
            "Gray" : [gray_squirrel],
            "Black" : [black_squirrel],
            "Cinnamon" : [cinnamon_squirrel]
        }
        
        data_dict = pandas.DataFrame(squirrelFurColorCounts)# sending results to new CSV
        data_dict.to_csv("./Pandas/Squirrel_Fur_Color_Counts")
        
        
if __name__ == "__main__":
    CSVManager.getSquirrelFur()