#!/usr/bin/python3

def sdef safe_print_integer(value):
    try:
        print('{:d}'.format(value), end="")
        return true
    except ValueError:
        return false