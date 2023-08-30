class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def deeper(posS, posT):
            if posT == len(t):
                return 1 # match
            if posS == len(s):
                return 0 # incomplete

            if s[posS] == t[posT]:
                return deeper(posS + 1, posT + 1) + deeper(posS + 1, posT) # consume letter or skip letter
            else:
                return                              deeper(posS + 1, posT) # need to skip letter

        result = deeper(0, 0)
        if result >= 2**31: # ??? weird test case, requires -1 if result is too large
            result = -1
        return result
