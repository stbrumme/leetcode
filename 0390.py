class Solution:
    def lastRemaining(self, n: int) -> int:
        gap   = 1
        left  = 1
        right = n
        dir   = True
        while left < right:
            length = 1 + ((right - left) // gap)
            if dir:
                left += gap
                if length % 2 == 1:
                    right -= gap
            else:
                right -= gap
                if length % 2 == 1:
                    left += gap

            dir  = not dir
            gap *= 2

        return left # or right