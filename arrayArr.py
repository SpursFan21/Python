import array as arr

input_string = input("Enter elements of the array separated by spaces: ")

array_data = [float(num) for num in input_string.split()]
x = arr.array("d", array_data)

print("\nArray List:")
for i in x:
    print(i, end=" ")
print("\n")

lenX = len(x)
minX = min(x)
maxX = max(x)
sumX = sum(x)
print(f"Length of Array is: {lenX}")
print(f"First element: {minX}")
print(f"Last element: {maxX}")
print(f"Sum of elements in list: {sumX}")
