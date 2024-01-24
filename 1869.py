class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        high = [ 0, 0 ]
        have = [ 0, 0 ]

        # let's play with Python's reduce()
        def merge(a, b):
            b = int(b)

            nonlocal have, high
            if a != b:
                have[b] = 0

            have[b] += 1
            high[b]  = max(high[b], have[b])
            return b

        reduce(merge, "?" + s) # prepend dummy element
        return high[1] > high[0]
