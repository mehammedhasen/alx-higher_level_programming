#!/usr/bin/python3
def no_c(my_string):
    """removes character c and C from string"""
    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements
    return new_string
