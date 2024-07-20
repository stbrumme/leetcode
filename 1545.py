class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # len(s_n) = 1, 3, 7, 15, ...
        #          = 2^1-1, 2^2-1, 2^3-1, 2^4-1, ...
        #          = 2^n-1

        # note: k is 1-based

        def deeper(n, k):
            # the digit in the middle is always "1", except when n == 1
            if n == 1:
                return 0

            size = (2 ** n) - 1
            mid  = size // 2 + 1

            if k == mid:
                return 1
            if k <  mid:
                return deeper(n - 1, k)                # left  side: same algorithm
            else:
                return deeper(n - 1, size - k + 1) ^ 1 # right side: flip index and result

        return str(deeper(n, k))
