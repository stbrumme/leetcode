class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def deeper(node):
            # constants
            if node.val == 0:
                return False
            if node.val == 1:
                return True

            # operations
            if node.val == 2:
                return deeper(node.left) or  deeper(node.right)
            else: # node.val == 3
                return deeper(node.left) and deeper(node.right)

        return deeper(root)
