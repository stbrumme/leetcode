class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        result = 0

        def deeper(node):
            if not node:
                return 0

            left    = deeper(node.left)
            right   = deeper(node.right)

            nonlocal result
            result += abs(left) + abs(right)   # coins moving in and out of subtrees

            return node.val + left + right - 1 # keep one coin in current node

        deeper(root)
        return result
