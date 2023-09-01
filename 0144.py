class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def deeper(node):
            if node:
                yield node.val
                yield from deeper(node.left)
                yield from deeper(node.right)

        yield from deeper(root)
