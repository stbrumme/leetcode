class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        val  = list(freq.values())
        high = max(val)
        return val.count(high) * high
