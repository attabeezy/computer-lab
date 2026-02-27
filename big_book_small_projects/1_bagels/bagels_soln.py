"""A deductive game where you must guess a number based on clues
Tags: short, game,  puzzle
Author: Attabeezy
Date: 26/02/2026"""

import random
import time

NUM_DIGITS = 3
MAX_GUESSES = 10


def getSecretNum():
    """Generates secret number from shuffling and selecting first NUM_DIGITS

    Returns:
        str: outputs first NUM_DIGITS of shuffled list of strings
    """
    numbers = list("1234567890")
    random.shuffle(numbers)
    
    secretNum = ''
    
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    
    return secretNum


def getClue(secretNum, guess):
    """
    if same return 'You got it'
    if same position return 'Fermi'
    if wrong position return 'Pico'
    if wrong retun 'Bagels'
    """
    
    if secretNum == guess:
        return 'You got it'
    
    clues = []
    
    for i in range(NUM_DIGITS):
        if secretNum[i] in guess[i]:
            return 'Fermi'
        elif secretNum[i] in guess:
            return 'Pico'
        
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
    
    return ' '.join(clues)

def getGuess():
    guess = ''
    possible = list('1234567890')
    random.shuffle(possible)
    
    for i in range(NUM_DIGITS):
        guess += possible[i]
    
    return guess

def computerGuess(secretNum):
    times = 0
    while True:
        start = time.time()
        guess = getGuess()
    
        if secretNum != guess:
            times += 1
        else:
            """print(f"{getClue(secretNum, guess)}, {secretNum}!")"""
            continue
    
        if secretNum == guess:
            stop = time.time()
            print(f"Don't worry it took me {times} guesses in {stop - start} seconds")
            break
        else:
            continue

def main():
    print(f"""Bagels, a deductive logic game.
          By Attabeezy
          
          I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          When I say:      That means:
            Pico           One digit is correct but in the wrong position.
            Fermi          One digit is correct and in the right position.
            Bagels         No digit is correct.
          
          For Example, if the secret number was 248 and your guess was 843, the
          clues would be Fermi Pico.""")
    
    
    while True:
        secretNum = getSecretNum()
        print("I have thought of a number!")
        print(f' You have {MAX_GUESSES} guesses to get it.')
        
        numGuess = 1
        while numGuess <= MAX_GUESSES:
            guess = ''
            
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuess}')
                guess = input('> ')
        
            clues = getClue(secretNum, guess)
            print(clues)
            numGuess += 1
        
            if guess == secretNum:
                break
            if numGuess > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secretNum}.")
                computerGuess(secretNum)
        
        print("Do you want to play again (yes or no): ")
        if not input('> ').lower().startswith('y'):
            break
    
        print("Thanks for playing!")
        
        
if __name__ == '__main__':
    main()