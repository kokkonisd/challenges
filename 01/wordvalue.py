from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    print "[Opening dictionary...]"
    dict_file = open(DICTIONARY, 'r')

    print "[Reading dictionary...]"
    data = dict_file.read()

    print "[Closing dictionary...]"
    dict_file.close()

    print "[Formatting data...]"
    words = data.split('\n');
    # Get rid of last element (will be an empty string)
    words.pop()

    print "[Done!]"
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    value = 0
    for letter in word:
        if letter.upper() >= 'A' and letter.upper() <= 'Z':
            value += LETTER_SCORES[letter.upper()]

    return value


def max_word_value(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if (not words):
        words = load_words()

    max = 0
    max_word = ''
    for word in words:
        if calc_word_value(word) > max:
            max = calc_word_value(word)
            max_word = word

    return max_word


if __name__ == "__main__":
    #pass # run unittests to validate
    max_word = max_word_value()
    print max_word, calc_word_value(max_word)
