class Solution:
    def deeper(self, root, track):
        if not root:
            return

        next = track + [ root.val ]
        if not root.left and not root.right:
            self.all.append(next)
        else:
            self.deeper(root.left,  next)
            self.deeper(root.right, next)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.all = []
        self.deeper(root, [])

        result = []
        for a in self.all:
            result.append("->".join(str(b) for b in a))
        return result
