class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def tilt(node):
            if not node:
                return 0

            l = tilt(node.left)
            r = tilt(node.right)
            result = node.val + l + r
            node.val = abs(l - r)
            nonlocal sum
            sum += node.val
            return result

        tilt(root)
        return sum
