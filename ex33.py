# while loops
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1

    print("numbers now:, numbers")
    print(f"At the bottom i is{i}")

print("The number:")

for num in numbers:
    print(num, end=' ')
