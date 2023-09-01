class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums = defaultdict(int)
        nums = defaultdict(int)

        def deeper(node, depth):
            if node:
                sums[depth] += node.val
                nums[depth] += 1
                deeper(node.left,  depth + 1)
                deeper(node.right, depth + 1)

        deeper(root, 0)
        return [ sums[i] / nums[i] for i in range(len(sums)) ]
