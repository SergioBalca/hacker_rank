#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n, represents the number of towers in the game
#  2. INTEGER m, represents the height of each tower
#

def towerBreakers(n, m):
    # Write your code here
    """ - Analizing different combinations, it can be concluded that every time the number of
        towers is even, player 2 wins. Otherwise, player 1 wins.
        - In the case where there is a tower with a height equal to 1, player 2 wins, because player 1
        can not make a move to begin with.
    """
    return 2 if n%2 == 0 or m==1 else 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
