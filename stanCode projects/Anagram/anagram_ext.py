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
    This program finds all anagrams of a given word.
    (This project does not utilized and recursion or backtracking, but its efficient for all words.)
    """
    print('Welcome to stanCode "Anagram Generator" (or ' + str(EXIT) + ' to quit)')
    while True:
        target = input('Find anagrams for: ').lower()
        start = time.time()
        if target == '-1':
            break
        else:
            len_int = int(len(target))
            dic = read_dictionary(len_int)
            results = []
            count = 0
            for word in dic:
                if find_anagrams_helper(list(target), list(word)):
                    print(word)
                    print('Searching...')
                    results.append(word)
                    count += 1
            print(str(count) + ' anagrams: ', end='')
            print(results)
            print('Searching...')
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(len_int):
    """
    This function transfer the dictionary file to a list.
    Notice that the dic only transfer the words having same length with the target word.
    :return: dic, the arranged dictionary.
    """
    dic = []
    with open(FILE, 'r') as f:
        for line in f:
            if len(line) == len_int + 1:
                # lst contains words in same length of len(s)
                dic.append(line.strip())
    return dic


def find_anagrams(s):
    """
    This function loop every possible words in dictionary, and compared the alphabet with the target word.
    :param s: str, the given word.
    """
    len_int = int(len(s))
    dic = read_dictionary(len_int)
    results = []
    count = 0
    for word in dic:
        if find_anagrams_helper(s, word):
            print(word)
            print('Searching...')
            results.append(word)
            count += 1
    print(str(count) + ' anagrams: ', end='')
    print(results)


def find_anagrams_helper(s, word):  # Compared if two words have same characters.
    if sorted(s) == sorted(word):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
