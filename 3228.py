class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        last   = 0
        ones   = 0
        for c in s:
            c = int(c)

            ones += c
            # move all 1s (step-by-step)
            if c == 0 and last == 1:
                result += ones

            last = c

        return result
