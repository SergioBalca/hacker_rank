#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    mtx_size = len(arr)
    idx = mtx_size - 1
    row = 0
    primary_diag = 0
    secundary_diag = 0

    while (row < mtx_size):
        column = 0
        while (column < mtx_size):
            if column == row:
                primary_diag += arr[row][column]
            if column == idx:
                secundary_diag += arr[row][column]
                idx -= 1
            column += 1
        row += 1
    return (abs(primary_diag - secundary_diag))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
