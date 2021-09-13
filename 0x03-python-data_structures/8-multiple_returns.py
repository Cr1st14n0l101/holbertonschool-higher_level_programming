#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None, 0
    return (len(sentence), sentence[0])
