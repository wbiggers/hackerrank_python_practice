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

# Logic - first - only calculate the square of each number once - when building the lists.
# Second - use itertools product to create all possible subsets.
# Third - use list comprehension to create a single list of the value of S for each combination
# Print max S.

from itertools import product


def square(num):
    return num**2


# Handle the input:
K, M = map(int, input().split())
N = []
for i in range(K):
    N.append(list(map(square, map(int, input().split()))))
    N[i].pop(0)

all_combos = product(*N)
S = list(sum(item) % M for item in all_combos)
print(max(S))
