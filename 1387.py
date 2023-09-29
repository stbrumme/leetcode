class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def power(n):
            if n == 1:
                return 0

            if n % 2 == 0:
                return 1 + power(n // 2)
            else:
                return 1 + power(3 * n + 1)

        # min-heap, "ordered" by power
        h = []
        for i in range(lo, hi + 1):
            h.append(( power(i), i ))
        heapify(h)

        # kick out smaller elements
        for _ in range(k - 1):
            heappop(h)
        # topmost
        return h[0][1]
