class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # process leaf: if it's True then the whole subtree is True
        if quadTree1.isLeaf:
            if quadTree1.val is True:
                return Node(True, True)
            else:
                return quadTree2

        # same as above, but the other way round
        if quadTree2.isLeaf:
            if quadTree2.val is True:
                return Node(True, True)
            else:
                return quadTree1

        # now we have an inner node, let's convert it's subnodes
        sub = []
        sub.append(self.intersect(quadTree1.topLeft,     quadTree2.topLeft))
        sub.append(self.intersect(quadTree1.topRight,    quadTree2.topRight))
        sub.append(self.intersect(quadTree1.bottomLeft,  quadTree2.bottomLeft))
        sub.append(self.intersect(quadTree1.bottomRight, quadTree2.bottomRight))

        # it's possible that all subtrees have the same value => convert to a leaf
        if all([ s.isLeaf for s in sub ]):
            if all([ s.val == sub[0].val for s in sub ]):
                return Node(sub[0].val, True)

        # recursion for the win
        return Node(False, False, sub[0], sub[1], sub[2], sub[3])
