class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # copied from problem 538
        sum = 0
        def deeper(node):
            if node:
                deeper(node.right)
                nonlocal sum
                sum += node.val
                node.val = sum
                deeper(node.left)

        deeper(root)
        return root
