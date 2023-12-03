class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = 0

        # keep track of min/max with two heaps
        low   = []
        high  = []
        # position of older item of current subarray
        start = 0
        for i, n in enumerate(nums):
            heappush(high, ( -n, i )) # min-heap
            heappush(low,  ( +n, i )) # max-heap

            # exceeding limit ?
            while -high[0][0] - low[0][0] > limit:
                # remove the older item
                if high[0][1] > low[0][1]:
                    start = max(start, 1 + heappop(low )[1])
                else:
                    start = max(start, 1 + heappop(high)[1])

            length = i - start + 1
            result = max(result, length)

        return result
