class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        return all((f & 1) == 0 for f in freq.values())
