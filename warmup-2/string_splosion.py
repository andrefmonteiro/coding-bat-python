'''
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def string_splosion(str):

    final_word = ""

    for i in range(len(str)):
        final_word += str[:i+1]
    
    return final_word