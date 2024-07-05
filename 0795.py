class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        result = 0

        def below(value):
            have = 0 # number of valid subarrays
            span = 0 # length of current subarray
            for n in nums:
                if n > value:
                    span  = 0
                else:
                    span += 1
                    have += span

            return have

        good  = below(right)    # all subarrays where max() <= right
        small = below(left - 1) # all subarrays where max() <  left
        return good - small
