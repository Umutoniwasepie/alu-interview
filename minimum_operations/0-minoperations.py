#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    if n <= 1:
        return 0

    operations = [float('inf')] * (n + 1)
    operations[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + (i // j))

    return operations[n] if operations[n] != float('inf') else 0

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

