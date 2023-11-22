class Solution:
    @cache
    def beautifulArray(self, n: int) -> List[int]:
        # up to n=10 you can brute force the problem
        # and will find many solutions, e.g. for 1 <= n <= 4:
        # n=1 (1)
        # n=2 (1, 2),    (2, 1)
        # n=3 (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2)
        #     (1, 3, 2, 4), (1, 3, 4, 2)
        # n=4 (2, 1, 4, 3)
        #     (2, 4, 1, 3), (2, 4, 3, 1)
        #     (3, 1, 2, 4), (3, 1, 4, 2)    <= interesting
        #     (3, 4, 1, 2)
        #     (4, 2, 1, 3), (4, 2, 3, 1)
        # somethings stands out:
        # - some solutions have all odd numbers first, then only even numbers
        #   - e.g. (3, 1, 4, 2)
        #   - the opposite is true if n is even, e.g. (4, 2, 1, 3) but never if n is odd
        #   - hence let's only consider the cases where "odds first"
        # - when looking only at these even numbers in the second half
        #   and dividing them by 2, then we get a solution for n//2
        # - it took me a while to realize that there is a similar pattern for the odd numbers:
        #   plus one then divided by two leads to a solution for n//2 as well
        # - e.g. (3, 1, 4, 2) => (3, 1) and (4, 2) => (3, 1) plus 1 div 2 and (4, 2) div 2 => (2, 1) and (2, 1)

        # basic cases
        if n <= 1:
            return [ 1 ]
        if n == 2:
            return [ 1, 2 ]

        left  = self.beautifulArray((n + 1) // 2)
        right = self.beautifulArray( n      // 2)
        return [ 2*l-1 for l in left ] + [ 2*r for r in right ]
