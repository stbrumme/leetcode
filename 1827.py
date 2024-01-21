class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        prev   = 0
        for n in nums:
            if n <= prev:
                prev   += 1
                result += prev - n
            else:
                prev    = n

        return result
