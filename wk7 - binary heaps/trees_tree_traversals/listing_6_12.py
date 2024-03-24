    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.left.preorder(self.root.leftChild)
        if self.rightChild:
            self.right.preorder(self.root.leftChild)
