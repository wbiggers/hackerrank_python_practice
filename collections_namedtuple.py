'''Task
Dr. John Wesley has a spreadsheet containing a list of student's ID's, marks, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.
Average = (sum of all marks)/(total students)
Notes:
1.  Columns can be in any order.  ID's, marks, class and name can be written in any order in the spreadsheet.\
2.  Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.

Input Format:
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs, name and class, under their respective column names.

Output Format:
Print the average marks of the list corrected to 2 decimal places.

Bonus:  Can you solve this challenge in 4 lines of code or less?
There is no penalty for solutions that are correct but have more than 4 lines.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Use namedtuple like a class with properties.
from collections import namedtuple

# Handle the input
N, total = int(input()), 0
student = namedtuple('student', input())
for i in range(N): total += int(student(*input().split()).MARKS)
print(total / N)


