class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        have = { c : i for i, c in enumerate(s) }
        return sum(abs(have[c] - i) for i, c in enumerate(t))
