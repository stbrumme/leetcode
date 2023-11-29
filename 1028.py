class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # split, use dummy ";" to separate numbers and dashes
        values = traversal.replace("-", ";-;").replace(";;", ";").split(";")
        pos    = 0

        def deeper(depth):
            nonlocal pos
            if pos == len(values):
                return None

            # expected depth ?
            d = 0
            while pos < len(values) and values[pos] == "-":
                d   += 1
                pos += 1
            if d != depth:
                # nope, go up
                pos -= d
                return None

            # "consume" value
            node = TreeNode(values[pos])
            pos += 1

            # process children recursively
            node.left  = deeper(depth + 1)
            node.right = deeper(depth + 1)
            return node

        return deeper(0)
