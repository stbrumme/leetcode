class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0

        # sliding window approach with a max-heap
        have = defaultdict(int)
        high = [] # max-heap
        left = 0
        for right, n in enumerate(nums):
            have[n] += 1

            # store new frequency
            heappush(high, ( -have[n], n ))
            while high and -high[0][0] > k:
                # remove outdated elements
                if -high[0][0] > have[high[0][1]]:
                    heappop(high)
                    continue
                # shrink sliding window
                l = nums[left]
                have[l] -= 1
                heappush(high, ( -have[l], l ))
                left += 1

            result = max(result, right - left + 1)

        return result
