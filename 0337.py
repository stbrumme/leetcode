class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def deeper(node, rob):
            if not node:
                return 0

            if rob:
                return deeper(node.left, False) + deeper(node.right, False) + node.val

            l = max(deeper(node.left,  True), deeper(node.left,  False))
            r = max(deeper(node.right, True), deeper(node.right, False))
            return l + r

        return max(deeper(root, True), deeper(root, False))
