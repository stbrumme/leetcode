class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n - 2 + 1):
            digits = []
            x = n
            while x > 0:
                digits.append(x % b)
                x //= b

            if digits != reversed(digits):
                return False
        return True
