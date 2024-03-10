# Python3 program to for tree traversals


# A class that represents an individual node in a
# Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# Then print the data of node
		print(root.val, end=" "),

		# Now recur on right child
		printInorder(root.right)


# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val, end=" "),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # The recur on right child
        printPostorder(root.right)

        # Now print the data of node
        print(root.val, end=" "),

# Driver code
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(30)
    root.left.right = Node(4)
    root.right.left = Node(25)
    root.right.right = Node(40)

    # Function call
    print("Inorder traversal of binary tree is")
    printInorder(root)
    print()

    print("Preorder traversal of binary tree is")
    printPreorder(root)
    print()

    print("Postorder traversal of binary tree is")
    printPostorder(root)


