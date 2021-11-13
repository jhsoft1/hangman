import random
import string
print('H A N G M A N')
play_or_exit = ''
while play_or_exit not in ['play', 'exit']:
    play_or_exit = input('Type "play" to play the game, "exit" to quit:')
if play_or_exit == 'exit': exit()
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
guess = '-' * len(word)
guesses = []
j = 1
while j <= 8:
    print('\n' + guess)
    letter = input('Input a letter: ')
    if len(letter) != 1:
        print('You should input a single letter')
    elif letter not in string.ascii_lowercase:
        print('Please enter a lowercase English letter')
    elif letter in guesses:
        print("You've already guessed this letter")
    elif letter in word:
        for i in range(len(word)):
            if word[i] == letter: guess = guess[:i] + letter + guess[i + 1:]
        if guess == word:
            break
    else:
        j += 1
        print("That letter doesn't appear in the word")
    guesses.append(letter)
if guess == word:
    print('You guessed the word', guess, '!\nYou survived!')
else:
    print('You lost!')
