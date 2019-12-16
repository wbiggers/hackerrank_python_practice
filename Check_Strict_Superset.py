"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the n sets.
Print True, if A is a strict superset of each of the n sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.

Input Format:
The first line contains the space separated elements of set A.
The second line contains integer n, the number of other sets.
The next n lines contains the space separated elements of the other sets.

Output Format:
Print True if set A is a strict superset of all other n sets. Otherwise, print False.
"""

A = set(input().split())
is_superset = True
n = int(input())

for _ in range(n):
    if not A > set(input().split()):
        is_superset = False
        break

print(is_superset)
