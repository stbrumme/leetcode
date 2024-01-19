class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        result = ""

        # map each character to its other case
        abc = "abcdefghijklmnopqrstuvwxyz"
        lower2upper = { c : c.upper() for c in abc }
        upper2lower = { c.upper() : c for c in abc }
        flip = lower2upper | upper2lower

        size = len(s)
        # iterate over all substrings
        for i in range(size):
            for j in range(size, i, -1):
                # needs to be longer
                if j - i <= len(result):
                    break

                current = s[i : j]
                if all(flip[c] in set(current) for c in current):
                    result = current

        return result
