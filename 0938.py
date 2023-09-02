class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def deeper(node):
            if not node:
                return 0

            children = deeper(node.left) + deeper(node.right)
            if node.val >= low and node.val <= high:
                return children + node.val
            else:
                return children

        return deeper(root)
