class Solution:
    def replaceDigits(self, s: str) -> str:
        shift = lambda c, x: chr(ord(c) + x)

        result = ""
        for i in range(0, len(s), 2):
            # copy at even indices
            c = s[i]
            result += c

            # modify at odd indices - if they exist
            if i + 1 < len(s):
                x = int(s[i + 1])
                result += shift(c, x)

        return result
