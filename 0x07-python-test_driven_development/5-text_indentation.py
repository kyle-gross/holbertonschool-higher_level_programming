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
    new_str = ""
    new_str2 = ""
    new_str3 = ""

    text_list = text.split(". ")
    for item in range(len(text_list)):
        if item < len(text_list) - 1:
            new_str += text_list[item] + '.\n\n'
        else:
            new_str += text_list[item]

    text_list2 = new_str.split("? ")
    for item in range(len(text_list2)):
        if item < len(text_list2) - 1:
            new_str2 += text_list2[item] + '?\n\n'
        else:
            new_str2 += text_list2[item]

    text_list3 = new_str2.split(": ")
    for item in range(len(text_list3)):
        if item < len(text_list3) - 1:
            new_str3 += text_list3[item] + ':\n\n'
        else:
            new_str3 += text_list3[item]

    print("{}".format(new_str3), end="")
