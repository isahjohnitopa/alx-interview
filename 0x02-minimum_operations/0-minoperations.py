#!/usr/bin/python3
"""
Contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in th files.
"""


def minOperations(n):
    """
    Function that calculate the needed n H characters in file
    Args:
        n: The number of H
    Returns:
        The minimum operation
    """
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations