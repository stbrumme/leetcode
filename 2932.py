class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            for y in nums:
                left  = abs(x - y)
                right = min(x, y)
                if left <= right:
                    result = max(result, x ^ y)
        return result
