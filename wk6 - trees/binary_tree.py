

"""
the constructor function expects to get some kind of object to store in the root.
Just like you can store any object you like in a list,
the root object of a tree can be a reference to any object.
"""

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

if __name__ == '__main__':
    print('hello tree')

    r = BinaryTree('a')
    print('root value: ', r.getRootVal())
    print('left child: ', r.getLeftChild())
    print('right child: ', r.getRightChild())
    print('---add left and right nodes')
    r.leftChild = BinaryTree('b')
    r.rightChild = BinaryTree('c')
    r.leftChild.leftChild = BinaryTree('d')
    r.leftChild.rightChild = BinaryTree('e')
    r.leftChild.leftChild.leftChild = BinaryTree('g')
    r.leftChild.leftChild.rightChild = BinaryTree('h')
    r.rightChild.rightChild = BinaryTree('f')

    preorder(r)
    print('---')
    postorder(r)
    print('---')
    inorder(r)

