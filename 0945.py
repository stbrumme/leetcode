class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        result = 0

        next = -1
        nums.sort()
        for n in nums:
            if n < next:
                result += next - n
            next = 1 + max(next, n)

        return result
