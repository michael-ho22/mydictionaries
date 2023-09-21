import csv

codes = {
    'A': '%', 'a': '9',
    'B': '@', 'b': '#',
    'C': '&', 'c': '5',
    'D': '$', 'd': '1',
    'E': '*', 'e': '8',
    'F': '!', 'f': '7',
    'G': '^', 'g': '6',
    'H': '-', 'h': '3',
    'I': '+', 'i': '2',
    'J': '=', 'j': '0',
    'K': ':', 'k': '/',
    'L': ';', 'l': '|',
    'M': '(', 'm': ')',
    'N': '[', 'n': ']',
    'O': '{', 'o': '}',
    'P': '<', 'p': '>',
    'Q': '.', 'q': ',',
    'R': '?', 'r': '_',
    'S': ' ', 's': '~',
    'T': '`', 't': '\'',
    'U': '"', 'u': '\\',
    'V': '!', 'v': '&',
    'W': '%', 'w': ':',
    'X': '?', 'x': '@',
    'Y': '|', 'y': '$',
    'Z': '^', 'z': '`'
}

infile = open('info_security.txt', 'r')

encrypted = open('encrypted.txt', 'w')

text = infile.read()

new_txt = ''
for letter in text:
    if letter in codes:
        new_txt += codes[letter]
    else:
        new_txt += letter

encrypted.write(new_txt)

encrypted.close()

