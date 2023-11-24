class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result = 0

        # in each turn, assign Alice the biggest pile of all remaining piles
        # we get the second pile
        # and Bob the smallest
        piles.sort(reverse = True)
        steps = len(piles) // 3
        for i in range(steps):
            pos = 2 * i + 1
            result += piles[pos]

        return result
