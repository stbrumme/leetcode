class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        # swapping a bit between two numbers only makes sense
        # if the bit is set in one number and not set in the other
        # since x * (y + a) = xy + xa
        # the product of x and y is minimized when bit a is set in the bigger number
        # => if x > y then set bit in x

        # we looking at the sequence [ 1, 2, 3, ..., 2^p-2, 2^p-1, 2^p ]
        # then I can rearrange it and create pairs:
        # [ 1, 2^p, 2, 2^p-1, 3, 2^p-2, ... ]
        # I can swap bits in each pair that it always becomes [ 1, 2^p-2 ]
        # except for [ 1, 2^p-1 ]
        # there will be (2^p) / 2 - 1 pairs
        modulo  = 1_000_000_007       # I hate problems which require modulo
        pairs   = (2**p) // 2 - 1     # number of pairs [ 1, 2^p-2]
        product = (2**p - 2) % modulo # product of each pair
        single  = (2**p - 1) % modulo # the only pair which is a bit different
        return (pow(product, pairs, modulo) * single) % modulo
