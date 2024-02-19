# function to reverse the letters in each word in a string
# maintaining the spaces between words, even if there are multiple spaces

import re
def reverse_words(text):
    # r signifies a raw string, so you don't have to use backslashes etc.
    # '( +)' string signifies any number of spaces.
    # The resulting string contains the spaces as list items.
    words = re.split(r'( +)', text)
    rev_text = ''.join(word[::-1] for word in words)
    print(rev_text)

reverse_words("My name is Alex")