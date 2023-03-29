#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            elem_1 = my_list_1[i]
        except IndexError:
            print("out of range")
            elem_1 = 0
        try:
            elem_2 = my_list_2[i]
        except IndexError:
            print("out of range")
            elem_2 = 0
        try:
            result = elem_1 / elem_2
            if isinstance(result, (int, float)):
                new_list.append(result)
            else:
                print("wrong type")
                new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        finally:
            elem_1 += 1
    return new_list
