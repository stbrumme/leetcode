class BSTIterator:
    def walk(self, node):
        if node:
            self.walk(node.left)
            self.inorder.append(node.val)
            self.walk(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.walk(root)

    def next(self) -> int:
        return self.inorder.pop(0)

    def hasNext(self) -> bool:
        return len(self.inorder) > 0
