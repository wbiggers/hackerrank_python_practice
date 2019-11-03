'''You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format:
The first line contains integer T, the number of test cases.
The next T lines contains the string S.

Output Format:
Print "True" or "False" for each test case without quotes.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

T = int(input())

for i in range(T):
    str = input()
    re_str = "r'" + str + "'"
    try:
        result = re.search(re_str, 'hello')
        print('True')
    except re.error:
        print('False')
