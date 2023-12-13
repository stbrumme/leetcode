class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = defaultdict(list)
        def read(node, depth):
            if node:
                if depth & 1:
                    values[depth].append(node.val)
                read(node.left,  depth + 1)
                read(node.right, depth + 1)

        def write(node, depth):
            if node:
                if depth & 1:
                    node.val = values[depth].pop()
                write(node.left,  depth + 1)
                write(node.right, depth + 1)

        read (root, 0)
        write(root, 0)
        return root
