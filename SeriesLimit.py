n = int(input("Enter the series limit: "))

if n != 0:
    for i in range(n):
        if i % 2 == 0: #we are increasing by 2
            if i == n - 2:# in this positon we alter the end to remove the final comma
                end = " "
            else:
                end = ", "
            print(i, end = end)#The end here allows us to print into a horizontal row
else:
    print("\nnot a valid number")