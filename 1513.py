class Solution:
    def numSub(self, s: str) -> int:
        result = 0

        ones = 0
        for c in s:
            if c == "1":
                ones   += 1
                result += ones
            else:
                ones    = 0

        return result % 1_000_000_007
