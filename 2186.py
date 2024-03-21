class Solution:
    def minSteps(self, s: str, t: str) -> int:
        have = [ 0 ] * 26
        a    = ord("a")
        for c in s:
            have[ord(c) - a] += 1
        for c in t:
            have[ord(c) - a] -= 1

        return sum(abs(h) for h in have)
