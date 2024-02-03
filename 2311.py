class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeros = ones = 0

        have  = 0
        shift = 0
        for c in reversed(s):
            have  += int(c) << shift
            shift += 1

            if   c == "0":
                zeros += 1    # accept every zero
            elif c == "1":
                if have <= k:
                    ones += 1 # accept ones if the result remains small

        return zeros + ones
