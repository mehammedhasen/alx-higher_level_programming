#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delate item at specific location """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
