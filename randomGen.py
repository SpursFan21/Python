import random

randNum = random.randint(1, 20)
print(f"Random number: {randNum}")

randNumList = [random.randint(1, 20) for _ in range(5)]# add brackets
print(f"Random numbers in range of 5: {randNumList}")
