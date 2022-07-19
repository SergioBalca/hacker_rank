#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    num_elements = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for element in arr:
        if element > 0:
            positive += 1
        if element < 0:
            negative += 1
        if element == 0:
            zero += 1
    print("{0:.6f}".format(positive / num_elements))
    print("{0:.6f}".format(negative / num_elements))
    print("{0:.6f}".format(zero / num_elements))
 
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
