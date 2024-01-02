class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0

        size = len(nums)
        for i in range(2 ** size):
            current = 0
            for j in range(size):
                if i & (1 << j):
                    current ^= nums[j]
            result += current
        return result
