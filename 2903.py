class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # brute force
        size = len(nums)
        for i in range(size):
            for j in range(i + indexDifference, size):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [ i, j ]

        return [ -1, -1 ]
