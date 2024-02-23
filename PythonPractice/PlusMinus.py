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
    # Initializing dictionary of the three counts we're looking for within the array
    plusminuscount = {'Positive': 0, 'Zero': 0, 'Negative': 0}
    
    # Iterating through the array and updating PlusMinus counts
    for value in arr:
        if value > 0:
            plusminuscount['Positive'] += 1
        elif value < 0:
            plusminuscount['Negative'] += 1
        elif value == 0:
            plusminuscount['Zero'] += 1

    # Return 
    return plusminuscount
    plusminuscount['Positive']/n

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))


    results = plusMinus(arr)
    pos_ratio = "{:.6f}".format(results['Positive']/n)
    zero_ratio = "{:.6f}".format(results['Zero']/n)
    neg_ratio = "{:.6f}".format(results['Negative']/n)
    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)

# Optimized Version of the code
#!/bin/python3

def plusMinus(arr):
    # Initializing counts
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # Iterating through the array and updating counts
    for value in arr:
        if value > 0:
            positive_count += 1
        elif value < 0:
            negative_count += 1
        else:
            zero_count += 1

    # Calculate ratios
    n = len(arr)
    pos_ratio = "{:.6f}".format(positive_count / n)
    zero_ratio = "{:.6f}".format(zero_count / n)
    neg_ratio = "{:.6f}".format(negative_count / n)

    # Print ratios
    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    # Call the function
    plusMinus(arr)