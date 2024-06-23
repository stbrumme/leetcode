class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        result = 0

        bad = 1 # lowest number we can't represent
        for c in sorted(coins) + [ target + 1 ]:
            while c > bad:
                # need to add a coin
                result += 1
                # choose the lowest value we couldn't represent
                bad    += bad

            bad += c

            if bad > target:
                break

        return result
