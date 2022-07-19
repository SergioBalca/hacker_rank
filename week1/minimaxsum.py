#!/bin/python3

from audioop import reverse
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    max_sum = 0
    min_sum = 0
    # For the min sum
    for idx, num in enumerate(arr):
        if idx != len(arr) - 1:
            min_sum += num

    arr.sort(reverse=True)
    #for max sum
    for idx, num in enumerate(arr):
        if idx != len(arr) - 1:
            max_sum += num
    print("{}  {}".format(min_sum, max_sum))
            
            


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)