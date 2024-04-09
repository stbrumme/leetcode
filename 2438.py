class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        bits = [] # exponents such that sum(2^bits[...]) = n
        for i in range(31):
            if n & (1 << i):
                bits.append(i)

        cache = {} # cache frequent values

        for q in queries:
            q = tuple(q)
            if q in cache:
                yield cache[q]
            else:
                left, right = q
                have  = sum(bits[left : right + 1]) # sum of exponents
                value = pow(2, have, 1_000_000_007)
                yield value
                cache[q] = value
