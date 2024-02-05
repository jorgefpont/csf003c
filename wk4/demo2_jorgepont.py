# Foothill College
# CS 03C - DSs and A in Python, Winter 2024
# Assignment 2
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Present run time test cases for lines 0 - 6 and
a final test case for line n for n the length of
your first name + the length of your last name
jorge pont is 5+4=9
"""

from jorgepontLab2 import pascal

y = 1
l = []

for n in [0, 1, 2, 3, 4, 5, 6, 9]:
    print('n = ', n)
    res = pascal(l, y, n)
    print('base of triangle: ', res)
    print('-----')

"""
PROGRAM OUTPUT
n =  0
base of triangle:  None
-----
n =  1
base of triangle:  [1]
-----
n =  2
base of triangle:  [1, 1]
-----
n =  3
base of triangle:  [1, 2, 1]
-----
n =  4
base of triangle:  [1, 3, 3, 1]
-----
n =  5
base of triangle:  [1, 4, 6, 4, 1]
-----
n =  6
base of triangle:  [1, 5, 10, 10, 5, 1]
-----
n =  9
base of triangle:  [1, 8, 28, 56, 70, 56, 28, 8, 1]
-----

Process finished with exit code 0
"""

"""
Recursive function stack example:
y=1, new_row=[1], num_rows=3, prev_row=[] ==> gets pushed to stack
y=2, new_row=[1,1], num_rows=3, prev_row=[1] ==> gets pushed to stack
y=3, new_row=[1,2,1], num_rows=3, prev_row=[1,1] ==> gets pushed to stack
y=4, new_row=None, num_rows=3, prev_row=[1,2,1] ==> gets pushed to stack

so full stack looks like (from top to bottom):
--------------------------------------------------
y=4, new_row=None, num_rows=3, prev_row=[1,2,1]
--------------------------------------------------
y=3, new_row=[1,2,1], num_rows=3, prev_row=[1,1]
--------------------------------------------------
y=2, new_row=[1,1], num_rows=3, prev_row=[1]
--------------------------------------------------
y=1, new_row=[1], num_rows=3, prev_row=[]
--------------------------------------------------

"""

