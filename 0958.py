# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        maxdepth = 0
        left     = root
        while left:
            maxdepth += 1
            left = left.left

        full = False
        def leaf(node):
            return node and not node.left and not node.right

        def last(node):
            if not node:
                return False

            nonlocal full
            if full:
                return not node.left and not node.right

            if not node.left:
                full = True
                return not node.right

            if not node.right:
                full = True
                return leaf(node.left)

            return leaf(node.left) and leaf(node.right)

        def deeper(node, depth):
            if depth < maxdepth - 1:
                if not node or not node.left or not node.right:
                    return False
                return deeper(node.left, depth + 1) and deeper(node.right, depth + 1)

            return last(node)

        return deeper(root, 1)