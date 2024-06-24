class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # trivial case
        if len(nums) == 1:
            return True

        # True if union-find of prime factors yield only one parent

        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # all 65 primes below sqrt(10^5)
        primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313 ]

        parent = { p: p for p in primes }

        # skip duplicates
        nums = set(nums)
        if 1 in nums: # avoid gcd() == 1
            return False

        for n in nums:
            if n not in primes:
                parent[n] = n

                # strip prime factors
                reduce = n

                # union all prime factors of n
                for p in primes:
                    while reduce % p == 0:
                        # prime factor
                        union(n, p)
                        reduce //= p

                    # found all factors
                    if reduce == 1:
                        break

                # last prime factor (might be larger than sqrt(10^5))
                if reduce > 1:
                    parent[reduce] = reduce
                    union(n, reduce)

        cycles = set()
        for n in set(nums):
            cycles.add(find(n))

        return len(cycles) == 1
