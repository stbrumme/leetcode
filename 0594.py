class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        best = 0
        for f in sorted(freq):
            if f+1 in freq:
                current = freq[f] + freq[f+1]
                best = max(best, current)

        return best