class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg =             bisect_left(nums, 0)
        pos = len(nums) - bisect_left(nums, 1, neg)
        return max(neg, pos)
