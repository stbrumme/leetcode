class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        level = {}
        above = {}
        def deeper(node, depth, parent):
            if node:
                level[node.val] = depth
                above[node.val] = parent
                deeper(node.left,  depth + 1, node.val)
                deeper(node.right, depth + 1, node.val)

        deeper(root, 0, None)
        return x in level and y in level and level[x] == level[y] and above[x] != above[y]
