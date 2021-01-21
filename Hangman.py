"""
SO THIS ONE WAS FROM A CODE SNIPPET SITE "pythonforbeginners.com
, and maybe with
some little editing, but it's not my original idea.
"""

import time

user_name= input("Enter your name: ")

time.sleep(0.5)

print('Welcome ',user_name)

word = 'bird'

print('guess the word, use only lowercase letters')


guesses = ' '

turns = 10

while turns > 0:

    for char in word:
        failed = 0

        if char in guesses:
            print(char)
        else:
            failed += 1
            print('_')

    if failed==0:
        print("You Won")
        break

    guess = input("Guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1

        print('Wrong')

        print('You have',  turns, 'more guesses')

        if turns == 0:
            print('You Lose')
