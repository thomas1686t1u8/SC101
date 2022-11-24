"""
File: hangman.py
Name: Thomas
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program creates a hangman game!
    Have fun!
    """
    answer = random_word()  # Create a random word.
    length = len(answer)
    turn = N_TURNS
    ans_string = ""
    for i in range(length):  # Print out the first word with "-".
        ans_string += '-'
    print("The word looks like " + str(ans_string))
    print('You have ' + str(turn) + ' wrong guesses left.')
    display(turn)
    while True:
        guess = input('Your guess: ').upper()  # Case insensitive.
        if guess.isalpha() and len(guess) == 1:  # If a valid guess is provided.
            if guess in answer:
                ans_string = hangman(guess, ans_string, answer)  # Update ans_string.
                print('You are correct!')
                if ans_string.isalpha():  # If the user get all the char of the answer.
                    break
                else:
                    print("The word looks like ", end="")
                    print(ans_string)
                    print('You have ' + str(turn) + '\r wrong guesses left.')
                    display(turn)
            else:  # A valid but wrong guess.
                turn -= 1  # Turn -1.
                print('There is no ' + str(guess) + "'s in the world")
                if turn == 0:
                    break
                print("The word looks like " + str(ans_string))
                print('You have ' + str(turn) + ' wrong guesses left.')
                display(turn)
        else:  # If an illegal guess is provided.
            print("Illegal format.")
    if turn == 0:  # If no turns left, print out the "fail" condition.
        display(turn)
        print('You are completely hung :(')
        print("The word was: " + str(answer))
    else:
        print("You win!!")  # If the user guess the answer, print out the "success" condition.
        print("The word was: " + str(answer))


def hangman(ch, ans_str, ans):
    """
    :Param ch: str, The guess of the user.
    :Param ans_str: str, The result includes all of the guess from the user.
    :Param ans: str, The correct answer.
    :return: str, A new result include this guess.
    """
    ans_str2 = ''
    for i in range(len(ans)):
        if ans[i] == ch:  # Search for the location of the right guess in the answer.
            ans_str2 += ch  # Added to the string.
        elif ans_str[i].isalpha():  # If the char already exists, preserve it.
            ans_str2 += ans_str[i]
        else:  # The remain char shown in "-".
            ans_str2 += '-'
    return ans_str2


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def display(n):
    if n == 0:
        print("--------")
        print("|      |")
        print("|     ( )")
        print("|     \\|/")
        print("|      |")
        print("|     / \\")
    elif n == 1:
        print("--------")
        print("|      |")
        print("|     ( )")
        print("|     \\|/")
        print("|      |")
        print("|     / ")
    elif n == 2:
        print("--------")
        print("|      |")
        print("|     ( )")
        print("|     \\|/")
        print("|      |")
        print("|")
    elif n == 3:
        print("--------")
        print("|      |")
        print("|     ( )")
        print("|     \\|/")
        print("|")
        print("|")
    elif n == 4:
        print("--------")
        print("|      |")
        print("|     ( )")
        print("|     \\|")
        print("|")
        print("|")
    elif n == 5:
        print("--------")
        print("|      |")
        print("|     ( )")
        print("|")
        print("|")
        print("|")
    elif n == 6:
        print("--------")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|")
    else:
        print("--------")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
