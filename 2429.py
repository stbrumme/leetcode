class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        flip = num2.bit_count()
        if flip == num1.bit_count():
            return num1 # unchanged

        bits = [ int(c) for c in bin(num1)[2 :] ] # strip "0b"
        size = max(num1, num2).bit_length()

        # prepend zeros
        while len(bits) < size:
            bits = [ 0 ] + bits

        # result
        x = [ 0 ] * size

        # flip leading ones to zeros
        for i in range(size):
            if bits[i] == 1 and flip > 0:
                x[i]  = 1 # so that 1 ^ 1 == 0
                flip -= 1

        # some bits still need to be flipped => flip trailing zeros to ones
        for i in reversed(range(size)):
            if bits[i] == 0 and flip > 0:
                x[i]  = 1
                flip -= 1

        # convert to integer
        result = 0
        for xx in x:
            result <<= 1
            result  |= xx
        return result
