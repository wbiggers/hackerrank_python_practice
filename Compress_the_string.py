"""
Task:
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive
occurrences of the character 'c' with (X, c) in the string. For a better understanding of the problem, check the
explanation.

Input Format:
A single line of input consisting of the string S.

Output Format:
A single line of output consisting of the modified string.
"""

from itertools import groupby

S = input()
S = list(S)

R = []
for key, group in groupby(S):
    tup = len(list(group)), int(key)
    R.append(tup)

print(*R)