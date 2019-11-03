'''Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed
only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is
subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of
students who have subscribed to at least one newspaper.

Input Format
The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.

Output Format
Output the total number of students who have at least one subscription.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

# initialize lists as sets
n_students = set()
b_students = set()

# collect input of English news students
n = int(input())
n_students.update(input().split())

# collect input of French news students
b = int(input())
b_students.update(input().split())

# create the union of English and French news students and count the number of entries in the union
print(len(b_students|n_students))

