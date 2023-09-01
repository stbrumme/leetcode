class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def deeper(node, isLeft):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if isLeft else 0

            return deeper(node.left, True) + deeper(node.right, False)

        return deeper(root, False)
