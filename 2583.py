class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = defaultdict(int)

        def deeper(node, depth = 0):
            if node:
                levels[depth] += node.val
                deeper(node.left,  depth + 1)
                deeper(node.right, depth + 1)

        deeper(root)
        sums = sorted(levels.values())
        return sums[-k] if k <= len(sums) else -1
