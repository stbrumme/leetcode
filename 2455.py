class Solution:
    def averageValue(self, nums: List[int]) -> int:
        three = [ n for n in nums if n % (2 * 3) == 0 ]
        return sum(three) // len(three) if three else 0
