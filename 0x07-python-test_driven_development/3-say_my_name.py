#!/usr/bin/python3
"""
prints first name and last name. Example:
    >>>say_my_name("John", "Smith")
    My name is John Smith
"""
def say_my_name(first_name, last_name=""):
    """
    Returns full name

    TypeError: first_name must be a string

    TypeError: last_name must be a string

    """
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

full_name = f"{first_name} {last_name}" if last_name else first_name
print(f"My name is {full_name}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()

