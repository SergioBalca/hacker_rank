#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    count_max = 0
    count_min = 0
    max_record = scores[0]
    min_record = max_record

    for i, score in enumerate(scores):
        if score > max_record:
            max_record = score
            count_max += 1
        if score < min_record and i != 0:
            min_record = score
            count_min += 1
        
    record_list = [count_max, count_min]
    return record_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
