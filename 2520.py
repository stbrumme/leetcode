class Solution:
    def countDigits(self, num: int) -> int:
        return sum(1 for c in str(num) if num % int(c) == 0)
