"""
Task:
A ridiculously complex description of the following problem.
Given a random list of numbers, every number in the list is repeated the same number of times in the list except for
one which is only listed once.  Find the number that is only appears once in the list.

Input:
The first line is an integer of the number of repeats that the numbers will have.
The second line is a space separated list of numbers in random order.

Output:
The number that is only listed once in the list.
"""

K = int(input())
numbers = list(map(int, input().split()))

