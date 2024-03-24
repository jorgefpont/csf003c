from stack_class import Stack
import string

def infix_to_postfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


if __name__ == '__main__':
    print(infix_to_postfix("( A + B ) * ( C + D )"))
    print('res: ', 'A B + C D + *')
    print(infix_to_postfix("( A + B ) * C"))
    print('res: ', 'A B + C *')
    print(infix_to_postfix("A + B * C"))
    print('res: ', 'A B C * +')