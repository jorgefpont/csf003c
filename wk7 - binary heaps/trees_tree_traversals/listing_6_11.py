def preorder(tree):
    if tree:
        print(tree.getRootKey())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())  
