#longest word finder
def longest(filename):
    with open(filename, "r") as file:
        words = file.read().split()
        
    max_len = len(max(words, key = len))
    return[word for word in words if len(word) == max_len]

print(longest("geek.txt"))