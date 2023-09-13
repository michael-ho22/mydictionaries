import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


'''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

mydictionary = {}

mydictionary = dict(m=8, n=9)

print(mydictionary)

phone = phonebook['chris']
print(phone)

print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()


name ='chris'

if name in phonebook:
    print(phonebook[name])
else:
    print(f'{name} is not in the phonebook')




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Joe'] = '555-0123'
phonebook['Chris'] = '555-444'

print(phonebook)

print()
print('*****  end section 3 ********')
print()





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


print(phonebook)

del phonebook['Chris']

print(phonebook)

print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for key in phonebook: ### this will only give  key
    print(f'The key is: {key} and the value is {phonebook[key]}')

for v in phonebook.values(): ### .values method gives just the values
    print(v)

for k,v in phonebook.items(): ###.items method gives a tuple, both key and value. It can be split if you give it two variables
    print(f'The key is {k} and the value is {v}')


print()
print('*****  end section 5 ********')
print()







print()
print('*****  start section 6 - using get and clear ********')
print()

print(phonebook)

phone = phonebook.get('chris', '911') ## if Chris is not found, will default result to not found

print(phone)

phonebook.clear() ## just clears out dictionary, doesn't delete it

print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
phone = phonebook.pop('Chris', 'not found') ### removes value out of dict

print(phone)
print(phonebook)


print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********') ## removes last element (last key and value)
print()

keyvalue = phonebook.popitem()

print(phonebook)




print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()


list_of_keys = list(phonebook) ##create a list of the keys
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))]) ## more efficient

print()
print('*****  end section 9 ********')
print()








