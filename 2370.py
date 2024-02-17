class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        chain = [ 0 ] * 26
        for c in s:
            id    = ord(c) - ord("a")
            left  = max( 0, id - k)
            right = min(25, id + k)
            chain[id] = 1 + max(chain[left : right + 1])

        return max(chain)
