class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        keys = sorted(freq)

        result = 0
        again  = 0
        for k in reversed(keys[1:]):
            result += freq[k] + again
            again  += freq[k]

        return result
