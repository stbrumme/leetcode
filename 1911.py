class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = odd = 0
        for n in nums:
            even, odd = max(even, odd - n), max(odd, even + n)
        return max(even, odd)
