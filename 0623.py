class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return None

        if depth == 1:
            return TreeNode(val, root, None)

        if depth > 2:
            self.addOneRow(root.left,  val, depth - 1)
            self.addOneRow(root.right, val, depth - 1)
            return root

        root.left  = TreeNode(val, root.left,  None)
        root.right = TreeNode(val, None, root.right)
        return root
