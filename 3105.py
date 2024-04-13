class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result = 1

        inc = dec = 1
        for a, b in zip(nums, nums[1 :]):
            if b > a: # increasing
                inc += 1
            else:
                inc  = 1

            if b < a: # decreasing
                dec += 1
            else:
                dec  = 1

            result  = max(result, inc, dec)

        return result
