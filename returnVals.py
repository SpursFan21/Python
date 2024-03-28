def add(a, b):
    return a + b

def isTrue(a):
    return bool(a)# returning boolin of a
reg = add(2, 3)
print("result of {}" .format(reg))
print(f"result of {reg:2f}")

reg = isTrue(2<5)
print(f"\n result of isTrue function is {reg:1f}")

