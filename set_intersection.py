"""
Task:
The students of District College have subscriptions to English and French
newspapers. Some students have subscribed only to English, some have subscribed
only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the
English newspaper, one set has subscribed to the French newspaper. Your task is
to find the total number of students who have subscribed to both newspapers.

Input Format:
The first line contains n, the number of students who have subscribed to the
English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the
French newspaper.
The fourth line contains b space separated roll numbers of those students.

Output Format:
Output the total number of students who have subscriptions to both English and
French newspapers.
"""

n = int(input())
nset = set(input().split())
b = int(input())
bset = set(input().split())

print(len(nset.intersection(bset)))
