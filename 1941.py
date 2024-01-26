class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        return min(freq.values()) == max(freq.values())
