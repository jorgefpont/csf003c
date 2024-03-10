# Foothill College
# CS 03C - DSs and A in Python, Winter 2024
# Assignment 4
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

from jorgepontLab4 import TreeNode, BinarySearchTree
from jorgepontLab4 import preorder, inorder, postorder, height

if __name__=='__main__':

    mytree = BinarySearchTree()

    l = [3, 2, 5, 1, 4, 6, 7]
    for e in l:
        mytree.put(e, None)

    print('Test that the keys were entered correctly:')
    print('root node: ', mytree.root.key)
    print('root left child: ', mytree.root.leftChild.key)
    print('root right child: ', mytree.root.rightChild.key)
    print('root left child left child: ', mytree.root.leftChild.leftChild.key)
    print('root right child left child: ', mytree.root.rightChild.leftChild.key)
    print('root right child right child: ', mytree.root.rightChild.rightChild.key)
    print('root right child right child right child: ', mytree.root.rightChild.rightChild.rightChild.key)
    print()
    print('number of elements: ', mytree.length())
    print('min key: ', mytree.find_min_key())
    print('max key: ', mytree.find_max_key())

    root = mytree.root
    print('tree height if root node is at height 1:', height(root))
    print('tree height if root node is at height 0:', height(root) - 1)
    print()
    print('inorder:')
    inorder(root)
    print('\npostorder')
    postorder(root)
    print('\npreorder:')
    preorder(root)
    print()

    print('\nProvide the Time and Space Complexity of your algorithm\n'
          'for finding the maximum element in the binary tree.\n')

    print('The time complexity for finding the max element in O(log n)\n'
          'The worse case of a fully unbanaced tree is O(n)')