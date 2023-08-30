class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        @cache
        def deeper(node, limit): # limit = max. direct child nodes
            if not node:
                return 0

            if not node.left and not node.right:
                self.best = max(self.best, node.val)
                return node.val

            l1 = deeper(node.left,  1)
            r1 = deeper(node.right, 1)
            l2 = deeper(node.left,  2)
            r2 = deeper(node.right, 2)
            me = node.val
            if limit == 1:
                result = max(me, me + l1, me + r1)
            else: # limit == 2
                result = max(me, me + l1, me + r1, me + l1 + r1)

            self.best = max(self.best, result)
            return result

        self.best = root.val
        deeper(root, 2)
        return self.best
