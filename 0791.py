class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        result = ""
        for c in order:
            result += c * freq[c]
            freq[c] = 0

        for c in freq:
            result += c * freq[c]

        return result
