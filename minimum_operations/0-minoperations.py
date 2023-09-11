#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""
import math


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0

    operations = 0
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        operations += n

    return operations
