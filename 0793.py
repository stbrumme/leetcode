class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # at zero at the end means that some numbers of the factorial have prime factor 5,
        # some have prime factor 2 (2*5=10). 2 is far more frequent, so only the 5s "complete" a 10.
        # f(x) = k means that there is exactly k times a 5
        # unfortunately a number may have several 5s as prime facators, e.g. 50 = 2 * 5 * 5

        # the result will either be 5 or 0:
        # if x is a multiple of 5 then f(x) = f(x+1) = f(x+2) = f(x+3) = f(x+4)
        # however if x is more than once a multiple of 5 then k jumps by more than 1
        # e.g. f(24) = 4 but f(25) = 6, there is no x such that f(x) = 5

        # edge case
        if k == 0:
            return 5

        # count trailing zeros of x
        def tens(x):
            result = 0
            while x > 0:
                x     //= 5
                result += x
            return result

        left  = 0
        right = 10 * k # rough estimate of upper bound
        while left < right:
            mid = (left + right) // 2
            if tens(mid) < k:
                left  = mid + 1
            else:
                right = mid

        # exact match => 5 numbers
        # not exact   => there's a jump and no f(x) = k
        return 5 * (tens(left) == k)
