class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def deeper(node):
            if node:
                yield from deeper(node.left)
                yield from deeper(node.right)
                yield node.val

        yield from deeper(root)
