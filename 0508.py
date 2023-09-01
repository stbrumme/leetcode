class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sums = defaultdict(int)

        def deeper(node):
            if not node:
                return 0

            current = node.val + deeper(node.left) + deeper(node.right)
            sums[current] += 1
            return current

        deeper(root)

        high = max(sums.values())
        return [ i for i in sums if sums[i] == high ]
