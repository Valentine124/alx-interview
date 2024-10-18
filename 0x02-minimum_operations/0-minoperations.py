#!/usr/bin/python3
"""
This module contains the solution of the
minoperation problem
"""

def minOperations(n):
    """ Returns the min number needed to result in exactly n"""
    cp = 1
    pst = 1
    operation = 0
    char = 1

    if n <= 0:
        return 0
    
    while True:
        if char == n:
            return operation
        if char > n:
            return 0
        if (n % char) == 0:
            operation += cp
            operation += pst
            char += char
            continue
        else:
            if (char * 2) > n:
                char += (n - char)
            else:
                char += char
            operation += pst
            continue