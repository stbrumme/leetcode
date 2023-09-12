class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def deeper(node, high):
            if not node:
                return 0

            l = deeper(node.left,  max(high, node.val))
            r = deeper(node.right, max(high, node.val))
            return l + r + (node.val >= high) # 1 if true

        return deeper(root, float("-inf"))
