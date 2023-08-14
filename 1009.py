class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        bits = []
        while n > 0:
            bits.append(n % 2)
            n >>= 1

        bits.reverse()
        for i in bits:
            n <<= 1
            n  += 1 - i

        return n
