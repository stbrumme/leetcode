class Solution:
    tracks = { }
    nodes  = { }
    relevant = []

    def getPath(self, root, track):
        if not root:
            return None

        next = track + [ root.val ]
        if root.val in self.relevant:
            self.tracks[root.val] = next
        self.nodes[root.val] = root

        self.getPath(root.left,  next)
        self.getPath(root.right, next)


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None

        self.relevant = [ p.val, q.val ]

        self.getPath(root, [])

        one = self.tracks[p.val].copy()
        two = self.tracks[q.val].copy()

        result = root
        while len(one) > 0 and len(two) > 0:
            if one[0] != two[0]:
                break

            result = self.nodes[one[0]]
            del one[0]
            del two[0]

        return result
