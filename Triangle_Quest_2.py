"""
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.
For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321

You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

Note:
Using anything related to strings will give a score of 0.
Using more than one for-statement will give a score of 0.

Input Format:
A single line of input containing the integer N.

Output Format:
Print the palindromic triangle of size N as explained above.
"""



for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    # My original code resulted in the correct answer - except that the conditions of the problem prevents a string
    # such as occurs with printing a list.
    # print(*list(range(1, i+1)) + list(range(i - 1, 0, -1)), sep='')

    # The mathematical answer is the series that results from 11^2 = 121, 111^2 = 12321, etc.  Basically need the number
    # of i '1's and then square that.
    print(((10 ** i - 1) // 9) * ((10 ** i - 1) // 9))