vowels = ['a','e','i','o','u']


word = 'apple'

#ctrl + f5
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)