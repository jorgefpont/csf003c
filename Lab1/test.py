"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.

Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
"""

from jorgepontstack import LinkedList


def is_match(p1, p2):  # I reversed
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = LinkedList()
    is_balanced = True
    index = 0

    if paren_string == "":
        return False

    while index < len(paren_string) and is_balanced:

        # print(index, paren_string[index])

        paren = paren_string[index]
        if paren in "([{":
        #if paren in ")]}":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

        # s.print_list()
        # print()
        # print("is empty: ", s.is_empty())
        # print("is_balanced: ", is_balanced)
        # print("---")

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

# 1.) Provide at least the 3 checks of balanced symbols:
test_case_1 = "([|)]"
test_case_2 = "() (() [()])"
test_case_3 = "{{([][])}()}"

print(is_paren_balanced(test_case_1))
print(is_paren_balanced(test_case_2))
print(is_paren_balanced(test_case_3))

# 2.) Provide a demonstration that your applications manages
# non symbol characters
print(is_paren_balanced("[[abc]]"))
print(is_paren_balanced("abc"))
# detects attempting to pop from an empty stack
print(is_paren_balanced(""))
# detects an incorrect pairing symbol popped from the stack

# 3.) Give the time and space complexity of your solution.
# time complexity:
# space complexity: