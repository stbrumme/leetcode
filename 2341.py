class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        one = 0 # singles
        two = 0 # pairs
        for f in freq.values():
            two += f // 2
            one += f &  1

        return [ two, one ]
