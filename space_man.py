#!/usr/bin/env python3

import random

# List of words from https://www.ef.edu/english-resources/english-vocabulary/top-100-words/
WORDS = ('a', 'about', 'all', 'also', 'and', 'as', 'at', 'be', 'because', 'but', 'by', 'can', 'come', 'could', 'day', 'do', 'even', 'find', 'first', 'for', 'from', 'get', 'give', 'go', 'have', 'he', 'her', 'here', 'him', 'his', 'how', 'I', 'if', 'in', 'into', 'it', 'its', 'just', 'know', 'like', 'look', 'make', 'man', 'many', 'me', 'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one', 'only', 'or', 'other', 'our', 'out', 'people', 'say', 'see', 'she', 'so', 'some', 'take', 'tell', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this', 'those', 'time', 'to', 'two', 'up', 'use', 'very', 'want', 'way', 'we', 'well', 'what', 'when', 'which', 'who', 'will', 'with', 'would', 'year', 'you', 'your')

def main():
    word = random.choice(WORDS) # Get a random word

    print(word) # Print word for debugging

    word_set = set(word) # Get all unique letters
    guesses = set() # Guesses unique

    game_over = False

    while not game_over:
        guess = get_letter_input()

        # While guess has been guessed
        while guess in guesses:
            print('You already guesed this letter')
            guess = get_letter_input()

        guesses.add(guess)
        guesses_left = 7 - len(guesses - word_set)

        print('You\'ve guessed {}'.format(', '.join(guesses)))
        print('You have {} guess(es) left'.format(guesses_left))
        print(' '.join(c if c in guesses else '_' for c in word))

        # All guesses in words
        if (guesses & word_set) == word_set:
            print('You win!')
            game_over = True
        # No more guesses
        elif not guesses_left:
            print('You lose')
            game_over = True
    print('Game over')

def get_letter_input():
    letter = input('Enter a letter: ')
    while len(letter) != 1 or not letter.isalpha():
        print('That\'s not a letter')
        letter = input('Enter a letter: ')
    return letter

def print_guesses(guesses):
    print('You\'ve guessed {}'.format(', '.join(guesses)))

if __name__ == '__main__':
    main()
