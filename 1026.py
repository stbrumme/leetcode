class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        def deeper(node, low, high):
            if node:
                nonlocal result
                result = max(result, abs(node.val - low), abs(high - node.val))

                low  = min(low,  node.val)
                high = max(high, node.val)
                deeper(node.left,  low, high)
                deeper(node.right, low, high)

        deeper(root, root.val, root.val)
        return result
