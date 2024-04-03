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

#read specific lines method 4

def fileRead(fname, nlines):
    with open(fname) as file:
        for i in range(nlines):
            line = file.readline()
            if not  line:
                break
            print(line, end="")
fileRead("geek.txt", 1)

#read line by line and store to list
file_path = "geek.txt"
line_list = []

with open(file_path, "r") as file:
    for line in file:
        line_list.append(line)
print(line_list)