class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(int)

        def deeper(node, depth):
            if node:
                levels[depth] += node.val
                deeper(node.left,  depth + 1)
                deeper(node.right, depth + 1)

        deeper(root, 1)

        high = max(levels.values())
        for i in levels:
            if levels[i] == high:
                return i
