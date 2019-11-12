"""
Task:
Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format:
The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Output Format:
Print the space separated elements of deque d.
"""

from collections import deque

d = deque()
for i in range(int(input())):
    command = list(input().split())
    if len(command) == 2:
        eval('d.%s(%d)' % (command[0], int(command[1])))
    else:
        eval('d.%s()' % command[0])

print(*list(d))
