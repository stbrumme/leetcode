class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)
        for a in s:
            freq[a] += 1
        for a in range(len(s)):
            if freq[s[a]] == 1:
                return a
        return -1
