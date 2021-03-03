def search4letters(phrase:str, letters:str='aeiou') -> set:
    '''Return any vowels found in a supplied phrases.'''
    return set(letters).intersection(set(phrase))




search4letters('hitch-hiker','aeiou')
search4letters('galaxy','xyz')
search4letters('life, the universe,and everything','o')
