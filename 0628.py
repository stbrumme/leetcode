class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        s = sorted(nums)
        return max(s[0]*s[1]*s[-1], s[-3]*s[-2]*s[-1])
