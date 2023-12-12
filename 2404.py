class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            if (n & 1) == 0:
                freq[n] += 1

        if freq:
            high = max(freq.values())
            for f in sorted(freq):
                if freq[f] == high:
                    return f

        return -1
