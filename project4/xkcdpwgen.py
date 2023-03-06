import argparse
import random

parser = argparse.ArgumentParser()

# arguments for -w or --words, default of 4 words in a password
parser.add_argument('-w', '--words', type=int, default=4,
help='include WORDS words in the password (default=4)')

# arguments for -c or --caps, no caps by default
parser.add_argument('-c', '--caps', type=int, default=0,
help='capitalize the first letter of CAPS random words (default=0)')

# arguments for -n or --numbers, no numbers by default
parser.add_argument('-n', '--numbers', type=int, default=0,
help='insert NUMBERS random numbers in the password (default=0)')

# arguments for -s --symbols, no symbols by default
parser.add_argument('-s', '--symbols', type=int, default=0,
help='insert SYMBOLS random symbols in the password (default=0)')

# getting each word from our words.txt file
dictionary = open('words.txt').read().splitlines()

# numbers have to be listed as strings so they can be appended
digits = (["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

# symbols, i.e. shift + all the numbers plus ~ . : and ;
symbols = (["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"])

# user inputs
input = parser.parse_args()

words = []
for i in range(0, input.words):
    if (input.caps > 0):
        words.append(random.choice(dictionary).capitalize())
        input.caps -= 1
    else:
        words.append(random.choice(dictionary))

password = []
for i in range(0, input.words):
    w = random.choice(words)
    words.remove(w)
    password.append(w)

while input.symbols > 0:
    s = random.choice(symbols)
    password.append(s)
    input.symbols -= 1

while input.numbers > 0:
    n = random.choice(digits)
    password.append(n)
    input.numbers -= 1

# shuffles the elements of the password
random.shuffle(password)
# returns the password
print("".join(password))