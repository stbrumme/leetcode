class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deeper(node):
            if not node:
                return None, 0

            l, ld = deeper(node.left)
            r, rd = deeper(node.right)

            # return deepest child node
            if ld > rd:
                return l, ld + 1
            if rd > ld:
                return r, rd + 1

            # both are the same, potential ancestor found
            return node, ld + 1 # ld == rd

        shared, depth = deeper(root)
        return shared
