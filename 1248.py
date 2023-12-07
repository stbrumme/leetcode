class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        have = 0 # current number of odd numbers in subarray [left, right]
        left = 0
        nice = 0 # nice subarrays in current sliding window
        for right, n in enumerate(nums):
            # new odd number
            if n & 1:
                have += 1
                nice  = 0

            # found a nice array, shift out odd number
            while have == k:
                have -= nums[left] & 1
                nice += 1
                left += 1

            if nice > 0:
                result += nice

        return result
