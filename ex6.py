types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
print(x)
print(y)

print(f"I said:{x}")
print(f"I also said:{y}")


hilarious = False
joke_evolution = "Isn't that joke funny? {}"    # 语句最后的“{}” 是一个标识符，在下一句中通过语法，替换为特定的内容
print(joke_evolution.format(hilarious))     # 本条中将变量hilarious 所指的 False 值，替换到上一句的{}处


w = "This is the left side of a string..."
e = "This is the right side of the string."
print(w + e)
