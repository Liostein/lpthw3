# modules classses Object
mystuff = {'apple': "I am apple."}
print
print(mystuff['apple'])

# a module name as mystuff.py has been created
import mystuff
mystuff.apple()

# mystuff['apple']  get apple from dict
# mystuff.apple()  get apple from the module
# mystuff.tangerine # same thing, it's just a variable

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I am classy apples!")

# a first class example

class Song(object): # make a class named Song that is-a object

    def __init__(self, lyrics): # class Song have-a __init__ that takes self and lyrics params
        self.lyrics = lyrics

    def sing_me_a_song(self): # classs have-a sing_me_a_song function that takes self parameter
        for line in self.lyrics:
            print(line)
happy_bday = Song(["Happy birtyday to you",
                   "I don't want to get sued",
                   "So i'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                       "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
