class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq = defaultdict(int)
        for c in word1:
            freq[c] += 1
        for c in word2:
            freq[c] -= 1

        return max(freq.values()) <= 3 and min(freq.values()) >= -3
