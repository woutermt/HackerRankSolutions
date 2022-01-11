#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(n, arr):
    uniques = set(arr)
    dupes = {}

    for i in uniques:
        dupes[i] = arr.count(i)

    return len(arr) - max(dupes.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()