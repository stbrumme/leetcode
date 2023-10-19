class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        total = defaultdict(int)
        def deeper(node, depth):
            if node:
                total[depth] += node.val
                deeper(node.left,  depth + 1)
                deeper(node.right, depth + 1)

        deeper(root, 0)
        return total[max(total)]
