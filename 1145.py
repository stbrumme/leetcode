class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        # idea: player 2 is free to choose his initial node
        # in order to cover the most nodes it's optimal to pick the best of these three nodes:
        # case A: parent of n
        # case B: left  children of n
        # case C: right children of n

        # three cases
        a = 0
        b = 0 # size of left  subtree of n
        c = 0 # size of right subtree of n

        def deeper(node):
            if not node:
                return 0

            left  = deeper(node.left)
            right = deeper(node.right)
            # A's initial node
            if node.val == x:
                nonlocal b, c
                b = left
                c = right

            return left + 1 + right

        # start counting
        deeper(root)

        # three cases
        total  = deeper(root)
        a = total - b - c - 1

        # no parent
        if x == root.val:
            parent = 0

        return 2 * max(a, b, c) > n
