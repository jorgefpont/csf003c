'''
Write a recursive function that accepts an integer argument n.
The function should display n lines of asterisks on the screen,
with the first line showing 1 asterisk,
the second line showing 2 asterisks,
up to the n-th line which shows n asterisks.
'''


def asterisk2(y, n):
    # base case
    if y > n:
        return
    else:
        print(y * '*')
        asterisk2(y + 1, n)


n = 5
y = 2
asterisk2(y, n)


def asterisk3(y, n):
    if y > n:
        return
    else:
        print(y * '*')
        asterisk3(y + 1, n)


asterisk3(y, n)
