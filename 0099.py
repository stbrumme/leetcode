class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # in-order traversal must be non-decreasing
        inorder = []
        def deeper(node):
            if node:
                deeper(node.left)
                inorder.append(node)
                deeper(node.right)

        deeper(root)

        # two elements are out of sync
        s = sorted([ x.val for x in inorder ])

        a = 0
        while inorder[a].val == s[a]:
            a += 1

        b = len(s) - 1
        while inorder[b].val == s[b]:
            b -= 1

        # swap
        inorder[a].val, inorder[b].val = inorder[b].val, inorder[a].val
