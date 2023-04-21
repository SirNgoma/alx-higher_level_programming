#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """returns sets of all elements present in only one set.
    Args:
        set_1: first set
        set_2: 2nd set
    """
    only_diff = set()

    for e in set_1:
        if e not in set_2:
            only_diff.add(e)
    for e in set_2:
        if e not in set_1:
            only_diff.add(e)

    return only_diff

