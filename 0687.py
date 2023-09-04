class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 0

        def deeper(node, value):
            if not node:
                return 0

            l = deeper(node.left,  node.val)
            r = deeper(node.right, node.val)

            godown = 0

            nonlocal result
            if value == node.val:
                # continue down
                length = 1 + max(l, r)
                result = max(result, length)
                godown = length

            # new path, connecting left and right
            length = 1 + l + r
            result = max(result, length)

            return godown

        deeper(root, float("inf"))
        return max(result - 1, 0)
