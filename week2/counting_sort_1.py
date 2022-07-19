#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    frecuency = [0] * 100
    for num in arr:
        frecuency[num] = frecuency[num] + 1
    return frecuency

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    frecuency = countingSort(arr)

    fptr.write(' '.join(map(str, frecuency)))
    fptr.write('\n')

    fptr.close()
