class Solution:
    def trailingZeroes(self, n: int) -> int:
        # count factors which are multiple of 5
        # (there are many more multiples of 2, no need to count them)
        result = 0
        for i in range(5, n+1, 5):
            n = i
            while n % 5 == 0:
                result += 1
                n //= 5

        return result
