class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left = {}

        def deeper(node, depth):
            if node:
                left[depth] = node.val
                # order matters !
                deeper(node.right, depth + 1)
                deeper(node.left,  depth + 1)

        deeper(root, 0)
        return left[max(left)]
