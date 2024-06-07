class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # True if all products can be distributed obeying the limit per store
        possible = lambda limit: n >= sum(ceil(q / limit) for q in quantities)
        # compute store needed per product, round up

        # avoid division-by-zero, start at 1
        return 1 + bisect_left(range(1, max(quantities) + 1), True, key = possible)
