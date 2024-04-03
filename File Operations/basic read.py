# read method 1

with open("geek.txt", "r") as file:
    for each in file:
        print(each)
        
# with read method 2
        
file = open("geek.txt", "r")
for each in file:
    print(each)
file.close()  # It's good practice to close the file after you're done with it.


#read method 3

file = open("geek.txt", "r")
print(file.read(3)) # this only reads a certain amount of characters from the left

