"""
You are given a function f(x) = x^2. You are also given K lists. The i-th list consists of Ni elements.
You have to pick one element from each list so that the value from the equation below is maximized:
S = (f(x1) + f(x2) + f(x3) + ... + f(xk)) % M
xi denotes the element picked from the i-th list . Find the maximized value Smax obtained.
% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares
of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to
the problem.

Input Format
The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the i-th list, followed by Ni space
separated integers denoting the elements in the list.

Output Format
Output a single integer denoting the value Smax.
"""

# Not knowing any math trick using modulo (no distributive property, etc.), use brute force methods.
# Logic - use itertools combinations to create all possible subsets. Calculate S for each.  Print max S.

# Handle the input:
K, M = map(int, input().split())
N = []
for i in range(K):
    N.append(list(map(int, input().split())))
    print(N)
    N[i].pop(0)
    print(N)




