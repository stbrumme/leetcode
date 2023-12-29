class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        result = 1

        last = 0
        size = 0
        for c in s:
            c = ord(c)
            if c == last + 1:
                size += 1
                result = max(result, size)
            else:
                size  = 1

            last = c

        return result
