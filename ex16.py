from sys import argv

script, filename = argv

print(f"We're going to erase{filename}.")
print(f"If you don't want that, hit control-C(^c).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file..")
target = open(filename, 'w')
# w mode will truncate your file first before writing
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these lines to the files.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# using one target.write only by format function:
# target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")

target.close()
