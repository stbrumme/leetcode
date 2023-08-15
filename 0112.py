class Solution:
    def deeper(self, root, sumSoFar, target):
        if not root:
            return False

        sumSoFar += root.val

        if not root.left and not root.right:
            return sumSoFar == target

        return self.deeper(root.left, sumSoFar, target) or self.deeper(root.right, sumSoFar, target)


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.deeper(root, 0, targetSum)
