class Solution:
    def preorder(self, root):
        if not root:
            return []

        return [ root.val ] + self.preorder(root.left) + self.preorder(root.right)


    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root

        flat = self.preorder(root)

        prev = None
        for i in flat:
            if prev:
                current = TreeNode(i, None, None)
                prev.right = current
            else:
                current = root
                current.left = current.right = None

            prev = current
