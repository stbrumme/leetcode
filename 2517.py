class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def possible(delta):
            need = price[0] + delta
            # pick next candy which costs at least "delta" more
            pos  = 0
            for _ in range(k - 1):
                pos = bisect_left(price, need, pos + 1)
                if pos == len(price): # no more candies
                    return False
                need = price[pos] + delta
            return True

        maximum = price[-1] - price[0]
        # look for first False =< its predecessor is the result
        return bisect_left(range(maximum + 1), True, key = lambda x : not possible(x)) - 1
