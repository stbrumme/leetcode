class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []

        remove = set(to_delete) # speed up

        def deeper(node):
            if not node:
                return None

            node.left  = deeper(node.left)
            node.right = deeper(node.right)

            if node.val in remove:
                result.append(node.left)
                result.append(node.right)
                return None

            return node

        result.append(deeper(root))
        # without None pointers
        for r in result:
            if r:
                yield r
