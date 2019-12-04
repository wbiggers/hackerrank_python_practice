"""
TASK:
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation
operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

Input Format:
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2*N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

Output Format:
Output the sum of elements in set A.
"""

_ = input()
A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    inst, Z = map(str, input().split())
    SZ = set(map(int, input().split()))
    eval('A.{}(SZ)'.format(inst))
print(sum(A))
