from os.path import exists
from sys import argv

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
# indata = open(from_file).READ()
# if you do open().read() , there is no need to close it in the end(line 25)
print(f"the input file is {len(indata)} bytes long.")

print(f"does the output file exist?", {exists(to_file)})
print("Ready? Hit RETURN to continue, CTRL-C to abort.")
input("> ")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
