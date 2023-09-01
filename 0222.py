class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # basic O(n) algorithm
        # solving in better than O(n) requires far mor code and is less versatile
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
