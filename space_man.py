import random


class SpaceMan():
    def __init__(self, words):
        self.word = random.choice(words)
        self.word_set = set(self.word)
        self.guesses = set()

    def run_game(self):
        game_over = False

        while not game_over:
            self.print_formatted_word()
            guess = self.get_letter_input()

            while guess in self.guesses:
                print('Already guesssed!')
                self.print_guesses()
                guess = self.get_letter_input()

            self.guesses.add(guess)

            self.print_guesses()

            if (self.guesses & self.word_set) == self.word_set:
                print('You win! Blast off!')
                game_over = True

            elif not self.guesses_left():
                print('You lose. Staying grounded :(')
                game_over = True

            print('-' * 32)
        print('Game over')

    def get_letter_input(self):
        letter = self.input_eof('Enter a letter: ').lower()

        while len(letter) != 1 or not letter.isalpha():
            print('That\'s not a letter')
            letter = self.input_eof('Enter a letter: ').lower()

        return letter

    # Handle CTRL+D or CTRL+Space to keep script alive
    def input_eof(self, prompt):
        try:
            return input(prompt)
        except EOFError:
            return self.input_eof('\nNice try: ')

    def print_formatted_word(self):
        print(' '.join(c if c in self.guesses else '_' for c in self.word))

    def print_guesses(self):
        print('You\'ve guessed', ', '.join(self.guesses))
        print('You have {} guess(es) left'.format(self.guesses_left()))

    def guesses_left(self):
        return 7 - len(self.guesses - self.word_set)

if __name__ == '__main__':
    # Word list from https://www.prdaily.com/Main/Articles/20880.aspx
    SpaceMan(('awkward', 'bagpipes', 'banjo', 'bungler', 'croquet', 'crypt', 'dwarves', 'fervid', 'fishhook', 'fjord', 'gazebo', 'gypsy', 'haiku', 'haphazard', 'hyphen', 'ivory', 'jazzy', 'jiffy', 'jinx', 'jukebox', 'kayak', 'kiosk', 'klutz', 'memento', 'mystify', 'numbskull', 'ostracize', 'oxygen', 'pajama', 'phlegm', 'pixel', 'polka', 'quad', 'quip', 'rhythmic', 'rogue', 'sphinx', 'squawk', 'swivel', 'toady', 'twelfth', 'unzip', 'waxy', 'wildebeest', 'yacht', 'zealous', 'zigzag', 'zippy', 'zombie')).run_game()
