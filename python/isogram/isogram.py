def is_isogram(string):
    '''An isogram is a word which has no
    repeating letters'''

    for char in string:
        if string.count(char) > 1:
            return False
    return True
