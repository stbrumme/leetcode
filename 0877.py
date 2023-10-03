class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def deeper(left, right):
            if left > right:
                return 0

            l = piles[left ] - deeper(left + 1, right)
            r = piles[right] - deeper(left, right - 1)
            return max(l, r)

        return deeper(0, len(piles) - 1)
