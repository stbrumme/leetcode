class Solution:
    def add(self, nums, begin, end):
        if not nums or begin >= end:
            return None

        mid = (begin + end) // 2
        left  = self.add(nums, begin, mid)
        right = self.add(nums, mid + 1, end)
        return TreeNode(nums[mid], left, right)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.add(nums, 0, len(nums))
