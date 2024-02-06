# Foothill College
# CS 03C - DSs and A in Python, Winter 2024
# Assignment 2
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994
# Note: used the homework from 3B/Fall-23
# the 3B assignment used recursion to draw
# a pyramid of asterisks

"""
Implement a recursion solution that takes a nonnegative integer n
as input and returns a list containing the sequence of numbers
appearing in the nth line of Pascal's triangle.
"""

triangle = []
def pascal(prev_row, y, num_rows):
    """Calculates a Pascal triangle and returns the base/bottom row
    Requires the following parameters:
    - prev_row should be an empty list, l=[]
    - y (int) is the number of elements in the top of the triangle, for this assignment y=1
    - num_rows (int) is how many rows the triangle should have
    Returns a list with the last row of the triangle"""

    if y > num_rows:  # base case
        return

    elif y < 3:
        new_row = y * [1]
        #print(new_row)
        triangle.append(new_row)
        pascal(new_row, y + 1, num_rows)

    else:
        new_row = []
        new_row.append(1)
        for i in range(1, y-1):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        #print(new_row)
        triangle.append(new_row)
        pascal(new_row, y + 1, num_rows)

    return triangle[-1]




