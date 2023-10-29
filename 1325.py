class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def deeper(node): # True if leaf that should be deleted
            if not node:
                return True

            l = deeper(node.left)
            r = deeper(node.right)

            # delete children
            if l:
                node.left  = None
            if r:
                node.right = None

            return node.val == target and l and r

        return None if deeper(root) else root
