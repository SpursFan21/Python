def createAdder(x):
    def adder(y):
        return x + y
    return adder
add15 = createAdder(15)
print(f"\nthe result is {add15(10)}")

def outer(x):
    return x * 10

def inner(y):
    return y * 10

def myFunc():
    return outer

def weFunc():
    return inner

reg = myFunc()
meg = weFunc()

print(f"\n the result is {reg(10)}\n")
print(f"\n the reult is {meg(15)}\n")