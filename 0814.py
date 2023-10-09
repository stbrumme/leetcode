class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deeper(node):
            if not node:
                return False

            one = (node.val == 1)
            l = deeper(node.left)
            if not l:
                node.left  = None

            r = deeper(node.right)
            if not r:
                node.right = None

            return one or l or r

        return root if deeper(root) else None
