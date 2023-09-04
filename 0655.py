class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getHeight(node):
            if node:
                return 1 + max(getHeight(node.left), getHeight(node.right))
            else:
                return -1

        height  = getHeight(root)
        rows    = height + 1
        columns = 2**(height + 1) - 1

        result = []
        for i in range(rows):
            result.append([ "" ] * columns)

        def deeper(node, x, y):
            if node:
                result[y][x] = str(node.val)
                step = 2**(height - y - 1)
                deeper(node.left,  x - step, y + 1)
                deeper(node.right, x + step, y + 1)

        deeper(root, columns // 2, 0)
        return result
