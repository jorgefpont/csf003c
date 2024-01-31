# Foothill College
# CS 03C - DSs and A in Python, Winter 2024
# Assignment 1
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994
# Note: used the homework from 3B/Fall-23
# for starter code and class definitions
# (Modified to use linked list instead of Python list
# and to push and pop from the right end

"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
"""

from jorgepontstack import LinkedList


def is_match(p1, p2):
    """Returns True if open and close parens match"""
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    """Returns True if an input string of parens is matched,
    False otherwise"""
    s = LinkedList()
    is_balanced = True
    index = 0

    if paren_string == "":
        return False

    while index < len(paren_string) and is_balanced:

        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


# 1.) Provide at least the 3 checks of balanced symbols:
case1 = "([|)]"
case2 = "() (() [()])"
case3 = "{{([][])}()}"
case4 = "[[abc]]"
case5 = "abc"
case6 = ""
case7 = "]"

test_cases = [case1, case2, case3, case4, case5, case6, case7]

for case in test_cases:
    print("Input string: ", case)
    print("Parens are balanced: ", is_paren_balanced(case))
    print('---')

# 2.) Provide a demonstration that your applications manages
# non symbol characters
# see case 4, 5 above

# detects attempting to pop from an empty stack
# see case6

# 3.) Give the time and space complexity of your solution.
# time complexity: O(n) as the program loops once through the input string

"""
C:\Users\jorge\PycharmProjects\CSF003C\venv\Scripts\python.exe C:\Users\jorge\PycharmProjects\CSF003C\Lab1\jorgepont1a.py 
Input string:  ([|)]
Parens are balanced:  False
---
Input string:  () (() [()])
Parens are balanced:  False
---
Input string:  {{([][])}()}
Parens are balanced:  True
---
Input string:  [[abc]]
Parens are balanced:  False
---
Input string:  abc
Parens are balanced:  False
---
Input string:  
Parens are balanced:  False
---
Input string:  ]
Parens are balanced:  False
---

Process finished with exit code 0

"""