class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0

        high = nums[0] # same as nums[i]
        diff = 0       # same as nums[i] - nums[j]
        for n in nums[1:]:
            result = max(result, diff * n) # (nums[i] - nums[j]) * nums[k]

            high = max(high, n)            # update nums[i]
            diff = max(diff, high - n)     # update nums[i] - nums[j]

        return result
