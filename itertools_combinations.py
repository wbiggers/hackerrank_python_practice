"""
Task:
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format:
A single line containing the string S and integer value k separated by a space.

Output Format:
Print the different combinations of string S on separate lines.
"""

from itertools import combinations

S, k = input().split()
S = list(S)
k = int(k)
S.sort()

C = []
for i in range(1, k + 1):
    C = C + list(combinations(S, i))

for item in C:
    print(''.join(item))