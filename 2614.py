class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def prime(x):
            # not prime by definition
            if x <= 1:
                return False

            # even
            if x % 2 == 0:
                return x == 2
            # odd
            i = 3
            while i*i <= x:
                if x % i == 0:
                    return x == i
                i += 2
            return True

        high = 0
        n = len(nums)
        for i in range(n):
            # \
            x = nums[i][i]
            if x > high and prime(x):
                high = x

            # /
            x = nums[i][(n - 1) - i]
            if x > high and prime(x):
                high = x

        return high
