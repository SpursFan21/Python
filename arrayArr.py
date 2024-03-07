import array as arr

x = arr.array("d", (23,34,54,34,77))
print("\n Array List :\n")

for i in x:
    print(i, end = " ")
print("\n")

lenX = len(x)
minX = min(x)
maxX = max(x)
sumX = sum(x)
print(f"Length of Array is {lenX}")
print(f"First element {minX}")
print(f"Last element {maxX}")
print(f"Sum of elements in list {sumX}")
