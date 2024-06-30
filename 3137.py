class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        size = len(word)

        freq = defaultdict(int)
        for i in range(0, size, k):
            freq[hash(word[i : i + k])] += 1

        return size // k - max(freq.values())
