class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        for n in nums:
            for c in str(n):
                yield int(c)
