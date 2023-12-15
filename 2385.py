class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        all = {}

        # walk down the tree
        def subtree(node, distance):
            nonlocal all
            if node and node.val not in all:
                all[node.val] = distance

                subtree(node.left,  distance + 1)
                subtree(node.right, distance + 1)

        # find start node
        def deeper(node):
            if not node:
                return None

            # found node
            if node.val == start:
                subtree(node, 0)
                return 0

            # scan children
            one = deeper(node.left)
            if one is not None:
                subtree(node, one + 1)
                return one + 1
            two = deeper(node.right)
            if two is not None:
                subtree(node, two + 1)
                return two + 1

            return None

        deeper(root)
        return max(all.values())
