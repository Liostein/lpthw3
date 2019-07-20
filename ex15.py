# Readlines
from sys import argv
script, filename = argv

txt = open(filename)

print(f"Here is your {filename}:")
print(txt.read())
# using argv get the filename is better than input, bcz argv can autocomplete
# print("type the filename again:")
#  file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())
