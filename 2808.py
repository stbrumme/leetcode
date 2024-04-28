class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        last = defaultdict(int)
        high = defaultdict(int)
        for i, n in enumerate(nums + nums):
            if n in last:
                high[n] = max(high[n], i - last[n])

            last[n] = i

        return min(high.values()) // 2
