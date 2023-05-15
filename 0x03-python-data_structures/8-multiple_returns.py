#!/usr/bin/python3

def multiple_returns(sentence):
    # Check if the sentence is empty
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    
    # Return a tuple with the length of the sentence and its first character
    return (len(sentence), first_char)
