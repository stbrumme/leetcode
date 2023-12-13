class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # each node value mapped to the sorted values of its two children
        def deeper(node, pairs):
            if node:
                if node.left and node.right:
                    one = node.left .val
                    two = node.right.val
                    pairs[node.val] = ( min(one, two), max(one, two) )
                elif node.left:
                    pairs[node.val] = ( node.left.val,  None )
                elif node.right:
                    pairs[node.val] = ( node.right.val, None )
                else:
                    pairs[node.val] = ( None, None )

                deeper(node.left,  pairs)
                deeper(node.right, pairs)

        # traverse both trees
        a = {}
        deeper(root1, a)
        b = {}
        deeper(root2, b)

        # compare all pairs
        if len(a) != len(b):
            return False
        for x in a:
            if x not in b:
                return False
            if a[x] != b[x]:
                return False

        return True
