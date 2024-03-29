    def evaluate(parseTree):
        opers = {'+':operator.add, '-':operator.sub, 
                 '*':operator.mul, '/':operator.truediv}
        leftC = parseTree.getLeftChild()
        rightC = parseTree.getRightChild()
        
        if leftC and rightC:              fn = opers[parseTree.getRootKey()]
            return fn(evaluate(leftC),evaluate(rightC))         else:
            return parseTree.getRootKey()
