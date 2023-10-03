class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        result = 0
        for f in freq:
            result += freq[f] * (freq[f] - 1) // 2 # triangle number, but freq[f]--
        return result
