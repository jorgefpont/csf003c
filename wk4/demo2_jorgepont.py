
from jorgepontLab2 import pascal
"""
Present run time test cases for lines 0 - 6 and 
a final test case for line n for n the length of 
your first name + the length of your last name
jorge pont is 5+4=9
"""

n = 8
y = 1
l = []

for n in [0, 1, 2, 3, 4, 5, 6, 9]:
    print('n = ', n)
    res = pascal(l, y, n)
    print('base of triangle: ', res)
    print('-----')
