import csv

newlist = []
dictionary = {}


infile = open('sometext.txt', 'r')

text = infile.read()
words = text.split()

print(type(words))
for word in words:
    word = word.lower()
    if word in newlist:
        if word in dictionary:
            dictionary[word] += 1 
    else:
        newlist += [word]
        dictionary[word] = 1

print(dictionary)