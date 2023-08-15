class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count bits, result will consists of bits which aren't multiples of 3
        bits = [0] * 32
        for i in nums:
            for j in range(32):
                if i & (1 << j):
                    bits[j] += 1

        result = 0
        for j in range(32):
            result += (bits[j] % 3) << j

        # two-complement
        if result >= 2**31:
            result -= 2**32
        return result
