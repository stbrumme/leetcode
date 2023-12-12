class Solution:
    def beautySum(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            have = [ 0 ] * 26
            for j in range(i, len(s)):
                c = ord(s[j]) - 97 # 97 = ord("a")
                have[c] += 1

                high = max(have)
                low  = min([ h for h in have if h > 0 ])
                result += high - low

        return result
