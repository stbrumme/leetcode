class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        # even though parts might be common, the longest whole sequence is never part of the shorter
        # if same length, then they can't be identical because of the check in the previous code line
        return max(len(a), len(b))
