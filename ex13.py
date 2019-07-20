from sys import argv
script, first, second, third = argv

print('THe script is called:', script)
print('Your first variable is called:', first)
print('Your second variable is called:', second)
print('Your third variable is called:', third)
# you should run this script in shell like:
# python ex13.py var1 var2 var3
# agrv[0] is the path name, so you just need input three variables

# argv is a sys funciton take all the arguments
# give these arguments to script before make it run
# input() get the value when the script running
