class Solution:
    def minOperations(self, s: str) -> int:
        # start with zero or one
        zero = 0
        one  = 0
        for i, c in enumerate(s):
            if i & 1 == int(c):
                one  += 1
            else:
                zero += 1
        return min(one, zero)
