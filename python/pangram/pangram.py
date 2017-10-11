def is_pangram():
    '''A function to determine if a given sentence is
    a pangram, a sentence using every letter of the 
    alphabet at least once.'''

    '''
    Start with all letters of the alphabet. As you
    loop over the test string 'string', remove a letter 
    from the alpabet list as you come to it. If all get removed,
    the string is a lambda.
    '''

is_pangram = lambda string: not set('abcdefghijklmnopqrstuvwxyz') - set(string.lower())