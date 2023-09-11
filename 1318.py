class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        while a > 0 or b > 0 or c > 0:
            if c & 1:
                result += 1 - ((a | b) & 1)
            else:
                result += a & 1
                result += b & 1

            a >>= 1
            b >>= 1
            c >>= 1

        return result
