class Solution:
    def minDeletions(self, s: str) -> int:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        reverse = defaultdict(int)
        for f in freq:
            reverse[freq[f]] += 1

        result = 0
        for high in range(max(reverse), 0, -1):
            if reverse[high] > 1:
                result            += reverse[high] - 1
                reverse[high - 1] += reverse[high] - 1
                reverse[high] = 1 # not needed

        return result
