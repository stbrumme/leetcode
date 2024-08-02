class Solution:
    # by far the hardest part is understanding the problem description
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, root)
        if root.val < val:
            return TreeNode(val, root)

        root.right = self.insertIntoMaxTree(root.right, val)
        return root
