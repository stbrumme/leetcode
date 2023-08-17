class Solution:
    def check(self, root, minn, maxx):
        if not root:
            return True

        if root.val <= minn:
            return False
        if root.val >= maxx:
            return False
        if not self.check(root.left, minn, root.val):
            return False
        if not self.check(root.right, root.val, maxx):
            return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float("-inf"), float("+inf"))
