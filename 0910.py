class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        # partition sorted values:
        # left side:  add k
        # right side: subtract k
        # in extreme cases, a side can be empty
        nums.sort()
        low    = nums[0]
        high   = nums[-1]
        result = high - low
        for split in range(1, len(nums)):
            up   = max(nums[split - 1] + k, high - k)
            down = min(nums[split    ] - k, low  + k)
            result = min(result, up - down)

        return result
