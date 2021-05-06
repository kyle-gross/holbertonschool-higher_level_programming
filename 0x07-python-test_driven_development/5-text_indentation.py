#!/usr/bin/python3
"""
This module contains the function text_indentation which prints
text with 2 new lines after each of these characters: '.', '?', and ':'
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:
    '.', '?', and ':'
    * <text> must be a string, otherwise raise a TypeError with message:
      "text must be a string"
    * There should be no space at the beginning or end of each printed line
    """
    # String check
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Print text
    text = text.replace(". ", ".\n\n")
    text = text.replace(": ", ":\n\n")
    text = text.replace("? ", "?\n\n")

    print(text)
