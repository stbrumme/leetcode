class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0

        # this is a math problem in its core (combinations)
        # and could be solved with almost no programming

        # but let's try to solve it with brute force

        if n > 3 * limit:
            return 0      # early exit: impossible

        # look at first child
        for one in range(min(n, limit) + 1):
            # candies given to children II & III
            other = n - one
            # maximum given to children II & III
            high  = min(limit, other)
            # minimum given to children II & III
            low   = other - high

            if low <= limit:
                result += high - low + 1

        return result
