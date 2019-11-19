"""
The object is to determine if it is possible to stack a series of elements in same or decreasing size.  However,
you can only take elements from the edge of the pile.

Input Format:
The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Output Format:
For each test case, output a single line containing either "Yes" or "No" without the quotes.
"""

# logic - if there is any number within the list that is larger than the two boundary numbers, you can never stack the
# numbers in order.

T = int(input())
for i in range(T):
    n = int(input())
    l = list(map(int, input().split()))
    if n <= 2:
        print('Yes')
    elif max(l[1 : -1]) > max(l[0], l[-1]):
        print('No')
    else:
        print('Yes')
