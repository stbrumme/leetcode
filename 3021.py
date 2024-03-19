class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd_n  = (n + 1) // 2
        even_n =  n      // 2

        odd_m  = (m + 1) // 2
        even_m =  m      // 2

        # sum i+j of each valid pair (i,j) must be odd
        return odd_n * even_m + even_n * odd_m
