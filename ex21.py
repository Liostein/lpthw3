def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"subtracting {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"multiplying {a} * {b}")
    return a * b


def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b


print("Let's do some math with jsut functions!")
# return 返回的值被赋值给左边的age等
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age:{age}, Height: {height}, Weight: {weight}, iq： {iq}")

# A puzzle
print("Here is a puzzle!")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")
