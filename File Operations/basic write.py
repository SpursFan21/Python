# basic write

file = open("geek.txt", "w")
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

# with write

with open("geek.txt", "w") as file:
    file.write("Hello World!")