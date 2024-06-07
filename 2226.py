class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # True if candies can be split into piles of size "size" each
        # and there are enough piles for all children
        def impossible(size):
            return sum(c // size for c in candies) < k

        # avoid size 0 => I should add 1 to the result
        # but actually we want the predecessor to the bisection position
        # so in the end they cancel each other
        total = sum(candies)
        if total < k:
            return 0
        return bisect_left(range(1, total + 1), True, key = impossible)
