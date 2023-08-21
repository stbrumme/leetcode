class Solution:
    def deeper(self, root, depth):
        if not root:
            return

        if not depth in self.maximum:
            self.maximum[depth] = root.val
        else:
            self.maximum[depth] = max(self.maximum[depth], root.val)

        if root.left:
            self.deeper(root.left,  depth+1)
        if root.right:
            self.deeper(root.right, depth+1)


    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.maximum = {}
        self.deeper(root, 0)

        result = []
        i = 0
        while i in self.maximum:
            result.append(self.maximum[i])
            i += 1

        return result
