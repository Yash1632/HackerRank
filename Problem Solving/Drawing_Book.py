#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    n_o_p = n-p+1
    if(n%2!=0):
        if(n_o_p<=(n/2+1)):
            pages = int((n_o_p-1)/2)
            #remain = (n_o_p-1) % 2
            return (pages)#+remain)
        else:
            pages = int((n-n_o_p)/2)
            remain = (n-n_o_p) % 2
            return (pages+remain)
    else:
        if(n_o_p<=(n/2)):
            pages = int((n_o_p-1)/2)
            remain = (n_o_p-1) % 2
            return (pages+remain)
        else:
            pages = int((n-n_o_p)/2)
            remain = (n-n_o_p) % 2
            return (pages+remain)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
