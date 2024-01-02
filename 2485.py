class Solution:
    def pivotInteger(self, n: int) -> int:
        all = n * (n + 1) // 2 # triangle number
        upper = 0
        for i in range(n, -1, -1):
            upper += i
            if upper == all:
                return i
            if upper >  all:
                return -1
            all   -= i
