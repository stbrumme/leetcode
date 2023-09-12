class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        best = 0

        @cache
        def deeper(node, goLeft):
            if not node:
                return 0

            l = deeper(node.left,  not goLeft)
            r = deeper(node.right, not goLeft)

            nonlocal best
            if goLeft:
                best = max(best, l)
                return l + 1
            else:
                best = max(best, r)
                return r + 1

        deeper(root, True)
        deeper(root, False)
        return best
