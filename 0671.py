class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # store all unique leaves
        result = set()

        def deeper(node):
            if not node:
                return

            if node.left and node.right:
                deeper(node.left)
                deeper(node.right)
            else:
                nonlocal result
                result.add(node.val)

        deeper(root)

        if len(result) < 2:
            return -1
        result.discard(min(result))
        return min(result)
