def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrases'."""
    return set(letters).intersection(set(phrase))




search4letters('hitch-hiker')
search4letters(letters='xyz',phrase='galaxy')
search4letters('life, the universe,and everything','o')
