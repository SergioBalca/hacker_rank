#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    round_grades = []
    for pos,grade in enumerate(grades):
        if grade >= 38:
            m_5 = grade + 2
            if m_5 % 5 == 0:
                round_grades.append(m_5)
            else:
                m_5 -= 1
                if m_5 % 5 == 0:
                    round_grades.append(m_5)
                else:
                    round_grades.append(grade)
        else:
            round_grades.append(grade)
    return (round_grades)
                        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
