#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with a lenght of a string and its first char.
    Args:
        sentence: sente to be worked on.
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
