class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digitsum = sum(int(c) for c in str(x))
        return digitsum if x % digitsum == 0 else -1
