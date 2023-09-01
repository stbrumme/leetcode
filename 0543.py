class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def deeper(node):
            l = r = 0
            if node.left:
                l = 1 + deeper(node.left)
            if node.right:
                r = 1 + deeper(node.right)

            self.result = max(self.result, l + r)
            return max(l, r)

        deeper(root)
        return self.result
