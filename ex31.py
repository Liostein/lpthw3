print("""You enter a dark room with two doors.
do you go through door #1 or door #2?""")

door = input(">  ")

if door == "1":
    print("""There is a giant bear here eating a cheese cake.
What do you do?
1. Take the cake.
2. Scream at the bear.""")

    bear = input(">  ")
    if bear == "1":
        print("The bear eats your face off.")
    elif bear == "2":
        print("The bear eat your leg off.")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear run away.")

elif door == "2":
    print("""You stare into the endless abyss at Cthulhu's retina.
    1. Bluberries.
    2. Yellow jaket clothespins.
    3. Understanding revolvers yelling melodies.""")

    insanity = input(">  ")
    if insanity == "1" or insanity == "2":
        print("Your bod survives powered by a mind of jello.\nGood job!")
    else:
        print("The insaniy rots your eyes into a pool of muck.\nGood job!")
else:
    print("You stumble around and fall on a knife and die.\nGood Job!")
