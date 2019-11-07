"""You are given two timestamps in the following format:  Day dd Mon yyyy hh:mm:ss +xxxx
Here +xxxx represents the time zone.
Your task is to print the absolute difference (in seconds) between them.

Input Format
The first line contains T, the number of test cases.
Each test case contains 2 lines, representing time t1 and time t2.

Output Format
Print the absolute difference (t1-t2) in seconds."""

# *******************************my own code***********************************************************************
# from time import strptime
# from calendar import timegm
#
#
# def conv_to_utc(t):
#     dow, dom, mon, yr, tm, tz = t.split()
#
    # create struct_time string
    # s = '%s %s %s %s %s' % (dow, mon, dom, tm, yr)

    # convert time zone to decimal form
    # tz = float(tz)
    # if tz < 0:
    #     tz = -1 * tz
    #     tz = (tz // 100) + ((tz % 100) / 60)
    #     tz = -1 * tz
    # else:
    #     tz = (tz // 100) + ((tz % 100) / 60)

    # calculate the time from the UTC epoch and add the time zone correction
    # return int(timegm(strptime(s)) - (tz * 3600))

# results = []
# T = int(input())
# for i in range(T):
#     t1 = conv_to_utc(input())
#     t2 = conv_to_utc(input())
#     results.append(abs(t2 - t1))

# for result in results:
#     print(result)

# ******************************************What they provided********************************************
# !/bin/python3

import math
import os
import random
import re
import sys
from time import strptime
from calendar import timegm


# Complete the time_delta function below.
def time_delta(t1, t2):
    rt1 = conv_to_utc(t1)
    rt2 = conv_to_utc(t2)
    return str(abs(rt2 - rt1))


def conv_to_utc(t):
    dow, dom, mon, yr, tm, tz = t.split()

    # create struct_time string
    s = '%s %s %s %s %s' % (dow, mon, dom, tm, yr)

    # convert time zone to decimal form
    tz = float(tz)
    if tz < 0:
        tz = -1 * tz
        tz = (tz // 100) + ((tz % 100) / 60)
        tz = -1 * tz
    else:
        tz = (tz // 100) + ((tz % 100) / 60)

    # calculate the time from the UTC epoch and add the time zone correction
    return int(timegm(strptime(s)) - (tz * 3600))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
