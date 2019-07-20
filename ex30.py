people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("Maybe we could take the trucks.")
elif trucks < cars:
    print("Maybe we should take the cars.")
else:
    print("FIne, let's stay home then.")
