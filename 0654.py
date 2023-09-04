class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        high = nums[0]
        pos  = 0
        for i in range(len(nums)):
            if high < nums[i]:
                high = nums[i]
                pos = i

        return TreeNode(high, self.constructMaximumBinaryTree(nums[:pos]), self.constructMaximumBinaryTree(nums[pos+1:]))
