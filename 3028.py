class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        return sum(not sum(nums[ : i + 1]) for i in range(len(nums)))
