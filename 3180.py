class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        size = len(rewardValues)
        high = max(rewardValues)

        @cache
        def deeper(have):
            # find next value greater than what we have
            pos = bisect_right(rewardValues, have)

            best = 0
            # try every bigger value, too
            while pos < size:
                next = deeper(have + rewardValues[pos])
                best = max(best, rewardValues[pos] + next)
                pos += 1

                # early exit
                if next == 0:
                    return max(best, high)

            return best

        return deeper(0)
