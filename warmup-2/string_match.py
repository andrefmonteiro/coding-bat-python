'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''

def string_match(a, b):

    count = 0
    small_str = a
    big_str = b
    if len(b) < len(a):
        small_str = b
        big_str = a
    

    for i in range(len(small_str) - 1):
        if small_str[i:i+2] == big_str[i:i+2]:
            count += 1
    
    return count
