def is_isogram(string):
    '''An isogram is a word which has no
    repeating letters'''

    # Validate that input is of String type
    if not isinstance(string, str):
        return False

    # If string is empty, no letters repeat so it passes
    if len(string) == 0:
        return True
    
    # Initialize variable
    isogram = True

    # Lowercase conversion to make case insensitive
    string = string.lower()

    # Ignore non-ascii characters to allow for spaces
    # and special characters to repeat

    for char in string:
        if string.count(char) > 1 and char.isalpha():
            isogram = False
    return isogram
