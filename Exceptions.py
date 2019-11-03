'''Task:
You are given two values a and b.
Perform integer division and print a/b.

Input Format:
The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.

Print the value of a/b.
In the case of ZeroDivisionError or ValueError, print the error code.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)
