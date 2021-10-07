#!/usr/bin/python3

"""
    Function that ident a sentence by . ? :
"""


def text_indentation(text):
    """
    Args:
        text: String with the sentence
    Raises:
        TypeError: If variable text is not an string
    Return:
        Void
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for signal in ".?:":
        text = (signal + "\n\n").join(sentence.strip(
            ' ') for sentence in text.split(signal))
    print(text, end="")
