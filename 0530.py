class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        all = []
        def deeper(node):
            if node:
                all.append(node.val)
                deeper(node.left)
                deeper(node.right)

        deeper(root)

        all.sort()
        all.append(float("inf"))

        result = float("inf")
        for i in range(len(all) - 1):
            result = min(result, all[i + 1] - all[i])

        return result
