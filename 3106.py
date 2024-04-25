class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        result = ""
        for c in s:
            # became immutable
            if k == 0:
                result += c
                continue

            # try to convert to "a"
            need = abs(ord(c) - ord("a"))
            if need > 13: # wraparound
                need = 26 - need

            # yes, "a" is within reach
            if 0 <= need <= k:
                result += "a"
                k -= need
            else:
                # always choose smallest possible character
                result += chr(ord(c) - k)
                k = 0

        return result
