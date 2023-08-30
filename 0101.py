class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(left, right):
            if not left and not right:
                return True
            if not left or  not right:
                return False

            if left.val != right.val:
                return False

            return same(left.left, right.right) and same(left.right, right.left)

        return same(root.left, root.right)
