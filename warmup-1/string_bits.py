'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''


def string_bits(str):

    final_word = ""

    for i in range(0, len(str), 2):
        final_word += str[i]

    return final_word
