people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5
if people >= dogs:
    print("People are greater or equal than dogs.")
if people <= dogs:
    print("People are less or equal than dogs.")

# = 是赋值。 == 是equal
if people == dogs:
    print("People are dogs.")
