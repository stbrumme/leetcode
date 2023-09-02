class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def deeper(node):
            if not node:
                return True
            if node.val != root.val:
                return False
            return deeper(node.left) and deeper(node.right)

        return deeper(root)
