class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        # idea. gcd(a, b) > 1 iff a and b share at least one prime factor

        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        have   = set(nums)
        high   = max(have)
        parent = [ i for i in range(high + 1) ]

        # all primes such that p^2 < 10^5
        primes = [ 2,   3,   5,   7,  11,  13,  17,  19,  23,  29,
                  31,  37,  41,  43,  47,  53,  59,  61,  67,  71,
                  73,  79,  83,  89,  97, 101, 103, 107, 109, 113,
                 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                 283, 293, 307, 311, 313 ]

        for n in nums:
            # factorize
            reduced = n
            for p in primes:
                if p * p > reduced:
                    break

                # merge all factors
                while reduced % p == 0:
                    union(n, p)
                    reduced //= p

            # largest prime factor
            if reduced > 1:
                union(n, reduced)

        # disjunct cycles must retain their positions
        for a, b in zip(nums, sorted(nums)):
            if find(a) != find(b):
                return False

        return True
