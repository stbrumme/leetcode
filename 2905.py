class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        size = len(nums)
        high = low = 0 # position, not actual values
        for i in range(indexDifference, size):
            # adjust high/low with old lagging values
            prev = i - indexDifference
            if nums[low]  < nums[prev]:
                low  = prev
            if nums[high] > nums[prev]:
                high = prev

            # compare against current value
            if abs(nums[i] - nums[low])  >= valueDifference:
                return [ low,  i]
            if abs(nums[i] - nums[high]) >= valueDifference:
                return [ high, i]

        return [ -1, -1 ] # failed
