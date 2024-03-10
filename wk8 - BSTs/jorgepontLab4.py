# Foothill College
# CS 03C - DSs and A in Python, Winter 2024
# Assignment 4
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

# code from class text:
# from: https://www.openbookproject.net/books/pythonds/Trees/SearchTreeImplementation.html

class TreeNode:
    """
    class for binary search tree node
    source from class text (see in pgm header)
    except as noted
    """

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:
    """
    class for binary search tree
    source from class text (see in pgm header)
    except as noted
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        """
        returns number of elements in the tree
        """
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

    def find_min_key(self):
        """
        I added to book code, to find min key in tree
        """
        current = self.root
        if current is None:
            return None

        while current.leftChild is not None:
            current = current.leftChild

        return current.key

    def find_max_key(self):
        """
        I added to book code, to find max key in tree
        """
        current = self.root
        if current is None:
            return None

        while current.rightChild is not None:
            current = current.rightChild

        return current.key

    def getRootKey(self):
        return self.root.key


mytree = BinarySearchTree()

l = [3, 2, 5, 1, 4, 6, 7]
for e in l:
    mytree.put(e, None)


def preorder(root_node):
    if root_node != None:
        print(root_node.key, end=" ")
        preorder(root_node.hasLeftChild())
        preorder(root_node.hasRightChild())


def inorder(root_node):
    if root_node != None:
        inorder(root_node.hasLeftChild())
        print(root_node.key, end=" ")
        inorder(root_node.hasRightChild())


def postorder(root_node):
    if root_node != None:
        postorder(root_node.hasLeftChild())
        postorder(root_node.hasRightChild())
        print(root_node.key, end=" ")


def height(root_node):
    if root_node is None:    # zero height
        return 0
    else:
        left_height = height(root_node.hasLeftChild())
        right_height = height(root_node.hasRightChild())

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1



# print('Test that the keys were entered correctly:')
# print('root node: ', mytree.root.key)
# print('root left child: ', mytree.root.leftChild.key)
# print('root right child: ', mytree.root.rightChild.key)
# print('root left child left child: ', mytree.root.leftChild.leftChild.key)
# print('root right child left child: ', mytree.root.rightChild.leftChild.key)
# print('root right child right child: ', mytree.root.rightChild.rightChild.key)
# print('root right child right child right child: ', mytree.root.rightChild.rightChild.rightChild.key)
# print()
# print('number of elements: ', mytree.length())
# print('min key: ', mytree.find_min_key())
# print('max key: ', mytree.find_max_key())
#
# root = mytree.root
# print('tree height if root node is at height 1:', height(root))
# print('tree height if root node is at height 0:', height(root) - 1)
# print()
# print('inorder:')
# inorder(root)
# print('\npostorder')
# postorder(root)
# print('\npreorder:')
# preorder(root)
# print()
#
# print('\nProvide the Time and Space Complexity of your algorithm\n'
#       'for finding the maximum element in the binary tree.\n')
#
# print('The time complexity for finding the max element in O(log n)\n'
#         'The worse case of a fully unbanaced tree is O(n)')
#
