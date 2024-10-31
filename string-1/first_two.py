'''
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
'''


def first_two(str):

    if len(str) < 2: # if check isn't necessary, as slicing is forgiving with index out of bounds
        return str
    return str[:2]
