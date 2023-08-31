class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        failed = float("inf")

        def deeper(node):
            if not node:
                return 0

            l = deeper(node.left)
            r = deeper(node.right)
            if l == failed or r == failed or abs(l - r) > 1:
                return float("inf")
            else:
                return 1 + max(l, r)

        return deeper(root) != failed
