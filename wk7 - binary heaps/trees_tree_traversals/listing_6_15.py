def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootKey())
        inorder(tree.getRightChild())
