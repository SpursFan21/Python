#ex1
def fun():
    str = "blabla"
    x = 20
    return str, x
str, x =fun()
print(str, x)

#ex2
tuple = 1, 2, 3
print(tuple)

#ex3
list = [1, 2, 3]
print(list)#full list
print(list[1])# list specific position

#ex4 Dict
dictionary = {"color": "red", "engine" : "V8", "Wheels": 32}
print(dictionary, "\n")

#ex5 list of Dict
listDictionary = [{"color": "red", "engine" : "V8", "Wheels": 32},
                  {"color": "blue", "engine" : "V6", "Wheels": 28},
                  {"color": "green", "engine" : "I6", "Wheels": 30}]
print(listDictionary, "\n")
print(listDictionary[1]["color"])