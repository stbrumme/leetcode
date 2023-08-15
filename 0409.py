class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        length = 0
        for f in freq:
            length += freq[f] // 2
        length *= 2

        for f in freq:
            if freq[f] % 2 == 1:
                length += 1
                break

        return length
