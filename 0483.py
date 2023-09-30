class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        result = n - 1 # each number n has good base n - 1

        # n = k^i + k^(i-1) + k^(i-2) + ... + k^2 + k + 1
        for i in range(2, 64):    # 10^18 < 2^64
            k = floor(n**(1 / i)) # i-th root of n
            if k == 1:
                break

            s = sum(k**j for j in range(i + 1))
            if s == n:
                result = k

        return str(result)
