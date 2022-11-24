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
from itertools import permutations

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program finds all anagrams of a given word.
    """
    print('Welcome to stanCode "Anagram Generator" (or ' + str(EXIT) + ' to quit)')
    while True:
        target = input('Find anagrams for: ').lower()
        start = time.time()
        if target == '-1':
            break
        else:
            print('Searching...')
            find_anagrams(target)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(len_int):
    """
    This function transfer the dictionary file to the data structure dic with the first three letters as key.,
    Notice that the dic only transfer the words having same length with the target word.
    :return: dic, the arranged dictionary.
    """
    dic = {}
    with open(FILE, 'r') as f:
        for line in f:
            if len(line) == len_int + 1:
                b = (line.strip())[0:3]
                if b in dic:
                    dic[b].append(line.strip())
                else:
                    dic[b] = [line.strip()]
    return dic


def find_anagrams(s):
    """
    This function check every possible permutations in the dictionary, and print out all anagrams.
    :param s: str, the given word.
    """
    len_int = int(len(s))
    dic = read_dictionary(len_int)
    # My own algorithm.
    all_anagrams = find_anagrams_helper(s, len(s), '', [], len_int, dic)
    # The built-in method in python, which is a little bit faster than mine.
    # all_anagrams = sorted([''.join(c) for c in permutations(s, len_int)])
    results = []
    count = 0
    for word in all_anagrams:  # Searching all permutations in the dictionary.
        b = word[0:3]
        if word[0:3] in dic:
            if word in dic[b]:
                if word in results:
                    pass
                else:
                    print(word)
                    print('Searching...')
                    results.append(word)
                    count += 1
    print(str(count) + ' anagrams: ', end='')
    print(results)


def find_anagrams_helper(word, word_len, current_word, results, len_int, dic):
    """
    This function finds all possible permutations of the given word.
    :param word: str, the given word.
    :param word_len: int, the length of the given word.
    :param current_word: str, the currently operating word.
    :param results: lst, the all possible permutations.
    :param len_int: int, the length of the given word.
    :param dic: dic, the dictionary.
    :return: lst, contains all of the possible permutations.
    """
    if len(current_word) == len_int:
        results.append(current_word)
    else:
        for i in range(word_len):
            if len(current_word) == 3:  # Check for early stop when the length is 3.
                if current_word not in dic:
                    break
            # Choose
            current_word += word[i]
            # Explore
            find_anagrams_helper(word[:i] + word[i+1:], word_len-1, current_word, results, len_int, dic)
            # Un-choose
            current_word = current_word[:-1]
    return results


def has_prefix(sub_s):
    """
    This function check the specific sub_string in the dictionary.
    However, I didn't use this function but use the similar concept instead in the algorithm.
    :param sub_s: str, the target sub string.
    :return: True or False.
    """
    switch = False
    dic = read_dictionary()
    for word in dic:
        if word.startswith(sub_s):
            switch = True
    return switch


if __name__ == '__main__':
    main()
