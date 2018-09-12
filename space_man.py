#!/usr/bin/env python3

import random

# List of words from https://www.ef.edu/english-resources/english-vocabulary/top-100-words/
WORDS = ('a', 'about', 'all', 'also', 'and', 'as', 'at', 'be', 'because', 'but', 'by', 'can', 'come', 'could', 'day', 'do', 'even', 'find', 'first', 'for', 'from', 'get', 'give', 'go', 'have', 'he', 'her', 'here', 'him', 'his', 'how', 'I', 'if', 'in', 'into', 'it', 'its', 'just', 'know', 'like', 'look', 'make', 'man', 'many', 'me', 'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one', 'only', 'or', 'other', 'our', 'out', 'people', 'say', 'see', 'she', 'so', 'some', 'take', 'tell', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this', 'those', 'time', 'to', 'two', 'up', 'use', 'very', 'want', 'way', 'we', 'well', 'what', 'when', 'which', 'who', 'will', 'with', 'would', 'year', 'you', 'your')

# Space Man game
def main():
    word = random.choice(WORDS) # Get a random word

    word_set = set(word) # Get all unique letters
    guesses = set() # Unique guesses

    game_over = False

    while not game_over:
        print_formatted_word(word, guesses)
        guess = get_letter_input()

        while guess in guesses:
            print('Already guesssed!')
            print_guesses(guesses)
            guess = get_letter_input()

        guesses.add(guess)
        guesses_left = 7 - len(guesses - word_set)

        print_guesses(guesses)
        print('You have {} guess(es) left'.format(guesses_left))

        # All guesses in words
        if (guesses & word_set) == word_set:
            print('You win!')
            game_over = True

        # No more guesses
        elif not guesses_left:
            print('You lose')
            game_over = True

        print('-' * 32)
    print('Game over')

def get_letter_input():
    letter = input_eof('Enter a letter: ').lower()

    while len(letter) != 1 or not letter.isalpha(): # Verify letter is single word char
        print('That\'s not a letter')
        letter = input_eof('Enter a letter: ').lower()

    return letter

# Handle CTRL+D or CTRL+Space to keep script alive
def input_eof(prompt):
    try:
        return input(prompt)
    except EOFError:
        return input_eof('\nNice try: ')

def print_formatted_word(word, guesses):
    print(' '.join(c if c in guesses else '_' for c in word))

def print_guesses(guesses):
    print('You\'ve guessed', ', '.join(guesses))

if __name__ == '__main__':
    main()
