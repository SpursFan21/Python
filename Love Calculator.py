print("Welcome to Duncan's Love Calculator")

try:
    name1 = str(input("Enter name 1: "))
    name2 = str(input("Enter name 2: "))
except ValueError:
    print("Invalid input. Please enter valid names.")
    exit()

# Convert names to lowercase before counting
name1_lower = name1.lower()
name2_lower = name2.lower()

#count the letters
count_t = name1_lower.count('t')
count_r = name1_lower.count('r')
count_u = name1_lower.count('u')
count_e = name1_lower.count('e')
count_t1 = name2_lower.count('t')
count_r1 = name2_lower.count('r')
count_u1 = name2_lower.count('u')
count_e1 = name2_lower.count('e')

#add up their score
LoveScore = count_t + count_r + count_u + count_e + count_t1 + count_r1 + count_u1 + count_e1

#generate report
if LoveScore >= 90 or LoveScore <= 10:
    report = "you go together very well"
elif 40 <= LoveScore <= 50:
    report = "you are alright together"
else:
    report = "you are not the best match for each other"

print(f"Your love score is {LoveScore}. {report}")

