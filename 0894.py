class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # each level has an even number of nodes plus there is one root node
        # => the total is always odd
        if (n & 1) == 0:
            return []

        if n == 1:
            return [ TreeNode() ]

        # each subtree has an even number of nodes
        result = []
        for i in range(1, n, 2):
            # all possible trees on the left side
            for left in self.allPossibleFBT(i):
                remaining = (n - 1) - i
                # and all on the right side, obeying the total number of nodes
                for right in self.allPossibleFBT(remaining):
                    # new root node
                    result.append(TreeNode(0, left, right))
        return result
