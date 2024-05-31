class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        digitsum = lambda x : sum(int(c) for c in str(x))

        # already beautiful ?
        if digitsum(n) <= target:
            return 0

        # convert digits to zeros, beginning from right side
        s = str(n)
        for i in range(len(s) - 1, -1, -1):
            left  = "0" + s[ : i]      # prepend a zero to avoid empty strings
            right =       s[i : ]

            left  = str(int(left) + 1) # increment by one
            right = "0" * len(right)   # all zeros
            s     = left + right       # and merge

            both  = int(s)
            if digitsum(both) <= target:
                return both - n
