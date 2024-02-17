class Solution:
    def largestPalindromic(self, num: str) -> str:
        have = [ 0 ] * 10
        for c in num:
            have[ord(c) - ord("0")] += 1 # faster than int(c)

        left = []
        if max(have[1 :]) > 1: # "outer" digits must not be zero
            for i in reversed(range(10)):
                while have[i] >= 2:
                    left.append(i)
                    have[i] -= 2
        left = "".join([ str(i) for i in left ])

        middle = ""
        for i in reversed(range(10)):
            if have[i] > 0:
                middle = str(i)
                break

        right = left[::-1]
        return left + middle + right
