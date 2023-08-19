class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        size = len(nums)
        bits = [0] * 32
        for n in nums:
            pos = 0
            while n > 0:
                if n & 1:
                    bits[pos] += 1
                pos += 1
                n  >>= 1

        result = 0
        for one in bits:
            zero = size - one
            result += one * zero

        return result
