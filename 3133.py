class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x

        # set all zero bits of x to the last number
        last = n - 1
        for i in range(64): # 64 bits is more than enough
            mask = 1 << i
            # zero bit found
            if not (x & mask):
                # copy bit
                if last & 1:
                    result |= mask
                last >>= 1

                # early exit
                if last == 0:
                    break

        return result
