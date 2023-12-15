class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # sum of subtree, including node itself
        @cache
        def subtree(node):
            return node.val + subtree(node.left) + subtree(node.right) if node else 0

        # sum of the whole tree
        total = subtree(root)

        result = 0
        def deeper(node):
            if not node:
                return 0

            one = subtree(node.left)
            two = subtree(node.right)

            best = max(one * (total - one), two * (total - two))
            best = max(best, deeper(node.left), deeper(node.right))
            return best

        return deeper(root) % 1_000_000_007
