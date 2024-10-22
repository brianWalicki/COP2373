# Reads a user inputted text of any reasonable length and prints
# the sentences and the number of sentences

import re

# Regular expression pattern to find sentences, with look ahead
pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

def main():

    # Starts counting sentences at 0
    count = 0
    s = input('Please enter the text. ')

    # Creates a list with all sentences from user input (s)
    m = re.findall(pat, s, flags=re.DOTALL | re.MULTILINE)

    # Prints all sentences and counts them
    for i in m:
        print('->', i)
        count+=1
    print(f'There are {count} sentences')

main()