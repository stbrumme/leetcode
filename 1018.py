class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = 0
        for n in nums:
            x <<= 1
            x  |= n
            x  %= 5
            yield x == 0
