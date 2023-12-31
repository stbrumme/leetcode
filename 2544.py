class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        sign   = +1
        for c in str(n):
            result += sign * int(c)
            sign    = -sign
        return result
