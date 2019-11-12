"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the
company name. They are now trying out various combinations of company names and logos based on this condition. Given a
string s, which is the company name in lowercase letters, your task is to find the top three most common characters in
the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
GOOGLE would have it's logo with the letters G O E.

Input Format:
A single line of input containing the string s.

Constraints
3 <= len(S) <= 10^4

Output Format:
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
"""

# ************************************************ Given Code Below ***************************************************
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby


if __name__ == '__main__':
    s = input()
# ************************************************ Given Code Above ***************************************************
    # First, get all similar letters together and count how many of each there are.  Use groupby and dictionary.
    # Sorting and then using OrderedDictionary means that the keys are already sorted in order for the print process later.
    d = {}
    sl = list(s)
    sl.sort()
    for key, group in groupby(sl):
        d[key] = len(list(group))

    # Get a list of all the frequencies of letters - this is a sorted list of the set of values - don't want repeats.
    freq = sorted(list(set(d.values())),reverse=True)
    ditems = list(d.items())
    x = 0
    pl = []
    f = 0
    while f < len(freq) and x < 3:
        item = 0
        while item < len(ditems) and x < 3:
            if ditems[item][1] == freq[f]:
                pl.append(ditems[item])
                x += 1
            item += 1
        f += 1

    for it in pl:
        print('%s %d' % (it[0], it[1]))
