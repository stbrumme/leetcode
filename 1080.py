class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def identify(node, sumFromRoot):
            if not node:
                return 0

            sumFromRoot  += node.val
            sumFromLeaves = 0

            l = identify(node.left,  sumFromRoot)
            r = identify(node.right, sumFromRoot)
            if node.left and node.right:
                sumFromLeaves = max(l, r)
            else:
                sumFromLeaves = r if node.right else l

            node.remove = (sumFromRoot + sumFromLeaves < limit)

            return sumFromLeaves + node.val

        def clear(node):
            if not node or node.remove:
                return None

            node.left  = clear(node.left)
            node.right = clear(node.right)
            return node

        identify(root, 0)
        return clear(root)
