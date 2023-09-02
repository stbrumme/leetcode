class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        levels = defaultdict(int)

        def count(node, depth):
            if node:
                levels[depth] += 1
                count(node.left,  depth + 1)
                count(node.right, depth + 1)

        count(root, 0)

        limit = max(levels)
        need  = levels[limit]
        result = None

        def locate(node, depth):
            if not node:
                return 0

            # early exit
            nonlocal result
            if result:
                return 0

            if depth == limit:
                if need == 1:
                    result = node
                return 1

            l = locate(node.left,  depth + 1)
            r = locate(node.right, depth + 1)
            if l + r == need and result == None:
                result = node
            return l + r

        locate(root, 0)
        return result
