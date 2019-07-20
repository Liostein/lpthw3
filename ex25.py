def break_words(stuff):
    """This funcion will break up words for us."""
    words = stuff.split(' ')
    return words
    # split returns a list of strings after breaking the given string by the specified sep
def sort_words(words):
    """Sort the words."""
    return sorted(words)

def print_first_word(words):
    """Print the first word after poppoing it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last words afters popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#try help(ex25) and help(ex25.break_words) in terminal
