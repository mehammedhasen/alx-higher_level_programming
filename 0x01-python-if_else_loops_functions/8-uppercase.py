#!/usr/bin/python3
def uppercase(str):
    for iterator in str:
        put = iterator
        if ord(put) >= 97 and ord(put) <= 122:
            put = chr(ord(iterator) - 32)
        print("{}".format(put), end='')
    print()
