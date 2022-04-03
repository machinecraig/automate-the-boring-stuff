# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 22:41:53 2022

@author: craig
"""

# This is a guess the number game

import random
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

# Ask the player to guess, give them 6 chances
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!
        
if guess == secretNumber:
    print('Good job!!! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry! The number I was thikning of was ' + str(secretNumber) + ' !')