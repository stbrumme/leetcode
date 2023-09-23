class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        shift  = 0
        for i in range(1, n+1):
            # exactly one bit set => bit representation just got longer
            if i & (i-1) == 0:
                shift += 1

            result <<= shift
            result  += i
            # avoiding large numbers which slow down the program
            result  %= 10**9 + 7

        return result