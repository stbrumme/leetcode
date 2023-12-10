class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        result = 0

        zero = 0
        ones = 0
        for c in s:
            if c == "0":
                if ones > 0:
                    # reset
                    zero = 0
                    ones = 0
                zero += 1
            else: # c == "1"
                ones += 1
                balanced = 2 * min(zero, ones)
                result   = max(result, balanced)

        return result
