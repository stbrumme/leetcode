class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def deeper(pos):
            if pos >= len(arr):
                return 0

            best = 0
            high = 0
            for i in range(k):
                index = pos + i
                if index >= len(arr):
                    break

                high = max(high, arr[index])
                best = max(best, (i + 1) * high + deeper(index + 1))

            return best

        return deeper(0)
