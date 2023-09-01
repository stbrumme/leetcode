class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right = { }

        def deeper(node, depth):
            if node:
                right[depth] = node.val
                deeper(node.left,  depth + 1)
                deeper(node.right, depth + 1)

        deeper(root, 0)
        return right.values()
