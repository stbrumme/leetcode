class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def deeper(left, right):
            if left >= right:
                return 0

            best = 9999999999
            choice = -1
            for mid in range(left, right + 1):
                l = deeper(left, mid - 1)
                r = deeper(mid + 1, right)
                current = mid + max(l, r)
                if best > current:
                    best = current
                    choice = mid
            return best

        return deeper(1, n)
