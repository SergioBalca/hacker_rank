#!/bin/python3

import math
import os
import random
import re
import sys

""" Library imported to create a dictionary, using the values of the array as keys
    and its frequency as dictionary values.
"""
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    """ with counter a dictionary with the values of the array as keys is created.
        The values are the frecuency of each value
    """
    a = Counter(a)
    max = 0
    
    """To evaluate the lenght of subarray that meets the criteria"""
    for k in sorted(a):
        m = a[k] + a.get(k+1,0)
        if max < m:
            max = m
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()