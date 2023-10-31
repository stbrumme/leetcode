class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def deeper(node, height):
            if not node:
                return True

            # search depth-first
            if not deeper(node.left,  height + 1) or \
               not deeper(node.right, height + 1):
                return False

            # check values
            if height % 2 == node.val % 2:
                return False

            # check level order
            if height % 2 == 0:
                if prev.get(height, float("-inf")) >= node.val:
                    return False
            else:
                if prev.get(height, float("+inf")) <= node.val:
                    return False

            # all fine
            prev[height] = node.val
            return True

        prev = {}
        return deeper(root, 0)
