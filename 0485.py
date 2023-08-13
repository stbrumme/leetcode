class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0

        current = 0
        for i in nums:
            if i == 1:
                current += 1
                result = max(result, current)
            else:
                current = 0

        return result
