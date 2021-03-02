#함수는 input필요없이 미리 받는다. (인자)
#함수는 리턴을 해야한다.

def search4vowels(word):
    '''Display any vowels found i an asked-for word.'''
    vowels = set('aeiou')
    #word = input('provide a word to search for vowels:')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


search4vowels('youmi')



##
def search4vowels(word):
    '''Display any vowels found i an asked-for word.'''
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)

search4vowels('youmi')  #youmi에 저 알파벳있으니 참

search4vowels('sky') #없으니 거짓

##################

def search4vowels(word):
    '''Return a boolean based on any vowels found'''
    vowels = set('aeiou')
    return vowels.intersection(set(word))

search4vowels('youmi')