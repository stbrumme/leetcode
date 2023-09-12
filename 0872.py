class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [ node.val ]
            return leafs(node.left) + leafs(node.right)

        return leafs(root1) == leafs(root2)
