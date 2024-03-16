class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        result = ""

        have = [ 0 ] * 128
        high = 0
        for c in s:
            ascii = ord(c)
            have[ascii] += 1
            if  high < have[ascii]:
                high = have[ascii]
                result  = c
            elif high == have[ascii]:
                result += c

        return result
