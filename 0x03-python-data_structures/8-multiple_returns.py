#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    firstCharacter = sentence[:1]
    # Return tuple with the length of string and first character
    return (length, firstCharacter)
