class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        size = len(prizePositions)

        # count consecutive prizes (within distance k)
        collect = []
        for i, left in enumerate(prizePositions):
            right = left + k
            pos = bisect_right(prizePositions, right)
            collect.append(pos - i)

        # the highest number of prizes of any segment where x >= prizePositons[i]
        best = [ 0 ] * (size + 1)
        for i in reversed(range(size)):
            best[i] = max(best[i + 1], collect[i])

        # for each segment, find the best starting after it ends
        result = 0
        for i in range(size):
            one = collect[i]
            two = best[i + one]
            result = max(result, one + two)

        return result
