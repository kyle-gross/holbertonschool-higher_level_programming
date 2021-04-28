#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        firstCharacter = None
    else:
        firstCharacter = sentence[:1]
    # Return tuple with the length of string and first character
    return (length, firstCharacter)
