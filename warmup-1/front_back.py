'''
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''

def front_back(str):

    if len(str) < 2:
        return str

    first_char = str[0]
    last_char = str[-1]

    return last_char + str[1:-1] + first_char
