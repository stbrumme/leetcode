class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        freq = [ 0 ] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1

        odd = 0
        for f in freq:
            odd += f & 1
        return odd <= k
