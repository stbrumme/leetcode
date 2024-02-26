class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Python's list can be surprisingly efficient at times ...
        mid   = k // 2 # middle of sliding window (position of median)

        right = k - 1
        have  = sorted(nums[ : right]) # initial window (without k-th value)
        while right < len(nums):
            insort(have, nums[right]) # add new value, keep list sorted

            median = have[mid] # assume k is odd
            if (k & 1) == 0:   # but maybe it's even ...
                median += have[mid - 1]
                median /= 2
            yield median       # emit

            # remove left-most value from the sorted list
            right += 1
            have.remove(nums[right - k]) # "slide out" value
