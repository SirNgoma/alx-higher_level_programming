#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurances of an element by aonother in anew list.
    Args:
        my_list: list to be worked.
        search: elem to replace
        replace: the new elem.
    """
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
