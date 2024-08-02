class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        result = 0

        # worst case: whole array's score > 0

        # in that case it can't be split into smaller subarrays (with the same score as the whole array)
        # because then the sum of scores isn't minimized anymore

        # therefore split into as many subarrays as possible with score 0 each

        # a number where all bits are set and which is larger than 10^6
        have = high = 0xFFFFFF
        for n in nums:
            have &= n
            # start a new subarray
            if have == 0:
                result += 1
                have    = high

        # if no subarrays with score 0 found, then the whole array can't be split
        return 1 if result == 0 else result
