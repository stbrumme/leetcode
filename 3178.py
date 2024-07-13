class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # basic simulation, avoid modulo math
        child     = 0
        direction = +1
        for _ in range(k):
            child += direction
            if child == n - 1 or child == 0:
                direction = -direction

        return child
