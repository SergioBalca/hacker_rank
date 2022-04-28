#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    my_dict = {'0': '1', '1': '0'}
    n_2 = format(n, '032b') # to convert to base 2 #
    inverse_s = ''
    for element in n_2:
        inverse_s += my_dict[element]
        flip_num = int(inverse_s, 2)
    return flip_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
