#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    """Height above sea level"""
    height = 0
    """Number of valleys in path"""
    valleys = 0
    """Flag that detects the start of a valley"""
    down_hill = 0
    
    for step in path:
        """If the next step is down at sea level a valley is detected"""
        if step == 'D' and height == 0:
            down_hill = 1
            height -= 1
        elif step == 'D':
            height -= 1
        elif step == 'U':
            height += 1
        """The hiker completes the valley when sea level is reach again"""
        if height == 0 and down_hill == 1:
            down_hill = 0
            valleys += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()