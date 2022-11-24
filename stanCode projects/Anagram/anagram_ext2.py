"""
File: anagram.py
Name: Thomas
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    The simplify version of anagram_ext.py.
    """
    print('Welcome to stanCode "Anagram Generator" (or ' + str(EXIT) + ' to quit)')
    while True:
        target = input('Find anagrams for: ').lower()
        start = time.time()
        if target == '-1':
            break
        else:
            dic = read_dictionary(target)
            for i in range(len(dic)):
                print('Searching...')
                print(dic[i])
            print(str(len(dic)) + ' anagrams: ', end='')
            print(dic)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(target):
    dic = []
    with open(FILE, 'r') as f:
        for line in f:
            if len(line) == len(target) + 1:
                # lst contains words in same length of len(s)
                word = line.strip()
                if sorted(word) == sorted(target):
                    dic.append(word)
    return dic


if __name__ == '__main__':
    main()
