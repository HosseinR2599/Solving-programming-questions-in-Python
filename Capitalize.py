import math
import os
import random
import re
import sys


def solve(s):
    # First we split the string into a list of words
    c = s.split()

    # Create an empty list to store words with the first letter capitalized
    words =[]

  
    if 0 < len(c) < 1000:

        # Process each word through a loop
        for k in c:

            # Capitalize the first letter of the word and add the rest unchanged
            capital_word = k.capitalize()

            # Add the processed word to the new list
            words.append(capital_word)

        # Convert the processed word list to a string
        result = ' '.join(words)
            
        return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
