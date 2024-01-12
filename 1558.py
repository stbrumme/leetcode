class Solution:
    def minOperations(self, nums: List[int]) -> int:
        bits = [ 0 ] * 32
        for n in nums:
            for i in range(32):
                if n < (1 << i): # just a performance optimization
                    break
                if n & (1 << i):
                    bits[i] += 1

        # eliminate unused bits
        while bits and bits[-1] == 0:
            bits.pop()

        # all zeros
        if not bits:
            return 0

        return sum(bits) + len(bits) - 1 # sum => add/op=0, len => shift/op=1
