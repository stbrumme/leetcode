class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for n in nums:
            if abs(result) > abs(n):
                result = n
                continue

            if abs(result) == abs(n) and result < n:
                result = n
        return result
