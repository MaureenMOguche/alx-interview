#!/usr/bin/python3
"""
This module defines a function that calculates the fewestnumber of 
operations needed to result in exactly n H characters in the a given file
"""


def minOperations(n):
    """
    returns the fewest number of operations needed to result in 
    exactly n H characters in a given file.
    """
    if type(n) is not int or n <= 1:
        return 0
    summation = []
    divisor = 2
    while (n % divisor) is 0 and (n // divisor) is not 1:
        summation.append(divisor)
        n = n // divisor
    divisor = 3
    while n > divisor:
        while (n % divisor) is 0 and (n // divisor) is not 1:
            summation.append(divisor)
            n = n // divisor
        divisor += 2
    summation.append(n)
    return sum(summation)
