def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words"""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Print the last word after poping it off."""
    word = words.pop(-1)
    print(word)


def sor_sentence(sentence):
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
    words = sor_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


if __name__ == '__main__':
    print(break_words("you are fat."))
    print(sort_words(break_words("you are fat.")))
    print_first_word(break_words("you are fat."))
    print_last_word(break_words("you are fat."))
    print(sor_sentence("you are fat."))
    print_first_and_last("you are fat.")
    print_first_and_last_sorted("you are fat.")
