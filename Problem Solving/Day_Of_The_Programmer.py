#!/bin/python

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = 0
    if(year>1918 and (year%400 == 0 or (year%4 == 0 and year%100 != 0))):
        months[1] = 29
    elif(year<1918 and year%4 == 0):
        months[1] = 29
    elif(year==1918):
        months[1] = 15
    j=0
    while(day<256):
        day = day+months[j]
        j = j+1
    day = months[j-1]-(day-256)
    
    if(j<10):
        return ""+str(day)+".0"+str(j)+"."+str(year)
    else:
        return ""+str(day)+"."+str(j)+"."+str(year)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(raw_input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
