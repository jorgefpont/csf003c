def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootKey())
        sVal = sVal + printexp(tree.getRightChild())+')'
    return sVal
