'''
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
'''


def non_start(a, b):
    # declare a version of A without first char
    # a_mod = a[1:]
    # declare a version of B wihtout the first char
    # b_mod = b[1:]
    # return their concatenation
    # return a_mod + b_mod

    # return the concatenation of their substrings
    return a[1:] + b[1:]